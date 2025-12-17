"""
Walks src/command/*.cpp and automation/autoload, extracts command names and their
menu/help strings, reads every *.po file in a directory, and produces
commands_32.yaml.

Usage:
    python generate_commands.py --cmd-dir path/to/src/command \
                                --lua-dir path/to/automation/autoload \
                                --po-dir  path/to/po \
                                --output commands_32.yaml
"""

import re
import argparse

from pathlib import Path

import polib
import yaml

STRUCT_RE = re.compile(r'\sstruct\s+(\w+)\s+final\s*:\s*public')
STRUCT_RECENT_RE = re.compile(r'\sstruct\s+(\w+)\s*:\s*public')
CLASS_RE = re.compile(r'class\s+(\w+):\s*public\s+([\w:]+)\s*\{')
LUA_RE = re.compile('tr"([^"]*)"')

STRING_RE = re.compile(r'(\w+)\("([^"]+)"\)')
CMD_NAME_RE = re.compile(r'CMD_NAME\("([^"]+)"\)')
STR_MENU_RE = re.compile(r'STR_MENU\("([^"]+)"\)')
STR_DISP_RE = re.compile(r'STR_DISP\("([^"]+)"\)')
STR_HELP_RE = re.compile(r'STR_HELP\("([^"]+)"\)')


def parse_scripts(source_dir: Path) -> dict:
    scripts = {}

    for lua_file in source_dir.rglob("*.lua"):
        text = lua_file.read_text(encoding="utf-8")
        filename = lua_file.stem

        search = LUA_RE.findall(text)
        script_name = search[0]
        script_description = search[1]

        cmd_name = f"automation/lua/{filename}/{script_name}"
        
        scripts[cmd_name] = {"display": script_name, "help": script_description}
    
    for moon_file in source_dir.rglob("*.moon"):
        text = moon_file.read_text(encoding="utf-8")
        filename = moon_file.stem

        search = LUA_RE.findall(text)
        script_name = search[0]
        script_description = search[1]

        cmd_name = f"automation/lua/{filename}/{script_name}"
        
        scripts[cmd_name] = {"display": script_name, "help": script_description}

    return scripts


def parse_commands(source_dir: Path) -> dict:
    """
    Scan all .cpp files under source_dir, return
    {cmd_name: {"display": display_src, "help": help_src}}
    """
    commands = {}

    for cpp_file in source_dir.rglob("*.cpp"):
        text = cpp_file.read_text(encoding="utf-8")

        # Find every struct that inherits from cmd::Command or a validator
        for m in STRUCT_RE.finditer(text):
            # Grab the block that belongs to this struct (until the first '}')
            block_start = m.end()
            block_end = text.find("}", block_start)

            if block_end == -1:
                continue

            block = text[block_start:block_end]

            name_match = STRING_RE.search(block)

            if not name_match:
                continue

            cmd_name = name_match.group(2)

            display_match = STR_DISP_RE.search(block) or STR_MENU_RE.search(block)
            display_src = display_match.group(1) if display_match else ""

            help_match = STR_HELP_RE.search(block)
            help_src = help_match.group(1) if help_match else ""

            # Workaround for these commands (they don't have STR_DISP or STR_MENU by default)
            match cmd_name:
                case "app/toggle/toolbar":
                    display_src = "Hide Toolbar"
                case "edit/redo":
                    display_src = "Nothing to redo"
                case "edit/undo":
                    display_src = "Nothing to undo"

            commands[cmd_name] = {"display": display_src, "help": help_src}

        # Find structs in recent.cpp
        for m in STRUCT_RECENT_RE.finditer(text):
            block_start = m.end()
            block_end = text.find("}", block_start)

            if block_end == -1:
                continue

            block = text[block_start:block_end]

            name_match = STRING_RE.search(block)

            if not name_match:
                continue

            cmd_name = name_match.group(2)

            display_match = STR_DISP_RE.search(block) or STR_MENU_RE.search(block)
            display_src = display_match.group(1) if display_match else ""

            help_match = STR_HELP_RE.search(block)
            help_src = help_match.group(1) if help_match else ""

            commands[cmd_name] = {"display": display_src, "help": help_src}

        # Find classes in video.cpp
        for m in CLASS_RE.finditer(text):
            block_start = m.end()
            block_end = text.find("}", block_start)
            if block_end == -1:
                continue
            block = text[block_start:block_end]

            name_match = STRING_RE.search(block)

            if not name_match:
                continue

            cmd_name = name_match.group(2)

            display_match = STR_DISP_RE.search(block) or STR_MENU_RE.search(block)
            display_src = display_match.group(1) if display_match else ""

            help_match = STR_HELP_RE.search(block)
            help_src = help_match.group(1) if help_match else ""

            commands[cmd_name] = {"display": display_src, "help": help_src}

    return commands


def load_po(po_path: Path) -> dict:
    """Return a dict mapping msgid -> translated msgstr."""

    po = polib.pofile(str(po_path))

    # Get non-translated msgids from the pot
    if ".pot" == po_path.suffix:
        return {entry.msgid: entry.msgid for entry in po}

    return {entry.msgid: entry.msgstr for entry in po}


def build_yaml(commands, locale_po_map, output_path: Path):
    """
    For every locale:
        * load its .po file
        * translate each command's display & help strings
        * write a YAML entry
    """

    locale_names = {
        "ar"          : "Arabic",
        "be"          : "Belarusian",
        "bg"          : "Bulgarian",
        "ca"          : "Catalan",
        "cs"          : "Czech",
        "da"          : "Danish",
        "de"          : "German",
        "el"          : "Greek",
        "en"          : "English",
        "es"          : "Spanish",
        "eu"          : "Basque",
        "fa"          : "Farsi",
        "fi"          : "Finnish",
        "fr_FR"       : "French",
        "gl"          : "Galician",
        "hu"          : "Hungarian",
        "id"          : "Indonesian",
        "it"          : "Italian",
        "ja"          : "Japanese",
        "ko"          : "Korean",
        "nl"          : "Dutch",
        "pl"          : "Polish",
        "pt_BR"       : "Portuguese (Brazilian)",
        "pt_PT"       : "Portuguese",  
        "ru"          : "Russian",
        "sr_RS"       : "Serbian (Cyrillic)",
        "sr_RS@latin" : "Serbian (Latin)",
        "vi"          : "Vietnamese",
        "zh_CN"       : "Chinese (Simplified)",
        "zh_TW"       : "Chinese (Traditional)"
    }

    yaml_entries = []

    for loc_code, po_path in sorted(locale_po_map.items()):
        translations = load_po(po_path)

        cmd_list = []
        for cmd_name, src in commands.items():
            raw_display = src.get("display")

            if translations.get(raw_display) != None and len(translations.get(raw_display)) > 0:
                display = translations.get(raw_display)
            else:
                display = raw_display

            raw_help = src.get("help")

            # Handle '\\\\' in strings like: 'Set the outline color (\\\\3c) at
            # the cursor position'
            if "\\\\" in raw_help:
                help_text = translations.get(raw_help.replace("\\\\", "\\"))
            else:
                if len(translations.get(raw_help)) > 0:
                    help_text = translations.get(raw_help)
                else:
                    help_text = raw_help

            # Handle display names for script commands
            if "/lua/" in cmd_name:
                splitted = cmd_name.split("/")
                splitted.pop()

                translated_name = "/".join(splitted) + f"/{ display }"

                entry = {"name": translated_name}
            else:
                entry = {"name": cmd_name}

            if display:
                entry["display"] = f"'{display}'"
            if help_text:
                entry["help"] = f"'{help_text}'"

            if "recent/" in cmd_name:
                for index in range(0, 16):
                    # Append 'recent/audio' first, then 'recent/audio/0'
                    if index == 0:
                        entry = {"name": f"{cmd_name[:-1]}", "display": f"'{display}'", "help": f"'{help_text}'"}
                        cmd_list.append(entry)

                    entry = {"name": f"{cmd_name}{index}", "display": f"'{display}'", "help": f"'{help_text}'"}
                    cmd_list.append(entry)
                continue

            cmd_list.append(entry)

        yaml_entries.append(
            {
                "locale": loc_code,
                "name": locale_names.get(loc_code, loc_code),
                "commands": sorted(cmd_list, key=lambda d: d["name"]),
            }
        )

    yaml_dump = yaml.dump(
                 yaml_entries,
                 allow_unicode=True,
                 sort_keys=False,
                 default_flow_style=False
                ).replace("'''", "'") # Handle yaml adding two additional apostrophes

    with output_path.open("w", encoding="utf-8") as f:
        f.write(yaml_dump)
    print(f"Wrote to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate commands.yml from Aegisub source & PO files.")
    parser.add_argument("--cmd-dir", required=True, help="Directory containing src/command/*.cpp")
    parser.add_argument("--lua-dir", required=True, help="Directory containing automation/autoload/*.lua|moon")
    parser.add_argument("--po-dir", required=True, help="Directory containing po/*.po")
    parser.add_argument("--output", default="commands_32.yaml", help="Output YAML file name")
    args = parser.parse_args()

    cmd_dir = Path(args.cmd_dir).resolve()
    lua_dir = Path(args.lua_dir).resolve()
    po_dir = Path(args.po_dir).resolve()
    output_path = Path(args.output).resolve()

    # Build a mapping of locale code -> .po path
    locale_po_map = {}
    for f in po_dir.iterdir():
        if f.suffix == ".pot":
            locale_po_map["en"] = f

        if f.suffix == ".po":
            loc_code = f.stem
            locale_po_map[loc_code] = f

    if not locale_po_map:
        raise RuntimeError(f"No .po files found in {po_dir}")

    commands = parse_commands(cmd_dir)
    scripts = parse_scripts(lua_dir)

    if not commands:
        raise RuntimeError("No commands found - did you point to the right 'src/command' directory?")

    if not scripts:
        raise RuntimeError("No scripts found - did you point to the right 'automation/autoload' directory?")

    commands.update(scripts)

    build_yaml(commands, locale_po_map, output_path)


if __name__ == "__main__":
    main()
