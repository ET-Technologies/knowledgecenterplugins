#!/usr/bin/env python3
"""Validate the repository's plugin manifests and shared component references."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAMES = ("knowledgecenter-gutachten", "knowledgecenter-energieausweis")
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def load_json(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8") as file:
        value = json.load(file)
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def require_file(plugin: Path, relative_path: str) -> None:
    path = plugin / relative_path.removeprefix("./")
    if not path.is_file() and not path.is_dir():
        raise ValueError(f"referenced path does not exist: {relative_path}")


def main() -> int:
    json_paths = sorted(
        path for path in ROOT.rglob("*.json") if ".git" not in path.parts
    )
    documents = {path: load_json(path) for path in json_paths}

    for expected_name in PLUGIN_NAMES:
        plugin = ROOT / expected_name
        claude = documents[plugin / ".claude-plugin" / "plugin.json"]
        codex = documents[plugin / ".codex-plugin" / "plugin.json"]

        for label, manifest in (("Claude", claude), ("Codex", codex)):
            if manifest.get("name") != expected_name:
                raise ValueError(f"{label} manifest name must be {expected_name!r}")
            version = manifest.get("version")
            if not isinstance(version, str) or not SEMVER.fullmatch(version):
                raise ValueError(f"{label} manifest version must be strict semver")

        if claude["version"] != codex["version"]:
            raise ValueError(f"{expected_name}: Claude and Codex versions must match")

        for field in ("skills", "mcpServers"):
            reference = codex.get(field)
            if not isinstance(reference, str):
                raise ValueError(f"Codex manifest field {field!r} must be a path")
            require_file(plugin, reference)

        apps = codex.get("apps")
        if apps is not None:
            if not isinstance(apps, str):
                raise ValueError("Codex manifest field 'apps' must be a path")
            require_file(plugin, apps)

        interface = codex.get("interface")
        if not isinstance(interface, dict):
            raise ValueError("Codex manifest interface must be an object")
        for field in ("composerIcon", "logo"):
            reference = interface.get(field)
            if not isinstance(reference, str):
                raise ValueError(f"Codex interface field {field!r} must be a path")
            require_file(plugin, reference)

    marketplace = documents[ROOT / ".agents" / "plugins" / "marketplace.json"]
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != len(PLUGIN_NAMES):
        raise ValueError("Codex marketplace must contain every plugin exactly once")
    entries = {entry.get("name"): entry for entry in plugins if isinstance(entry, dict)}
    if set(entries) != set(PLUGIN_NAMES):
        raise ValueError("Codex marketplace plugin names do not match the folders")
    for entry in entries.values():
        if "interface" in entry:
            raise ValueError(
                "plugin display metadata belongs to the marketplace interface"
            )

    print(
        f"Validated {len(json_paths)} JSON files and {len(PLUGIN_NAMES)} plugin packages."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
