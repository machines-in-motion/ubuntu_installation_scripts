"""Select the default boot option used by GRUB.

Parses /boot/grub/grub.cfg to list all available boot options (typically the installed
kernel versions) and let's the user select one to be set as default.
Based on the user's selection, GRUB_DEFAULT in /etc/default/grub is updated.  Note that
you still need to run `update-grub` afterwards to apply the changes.
"""

from __future__ import annotations

import argparse
import curses
import re
import sys
from difflib import unified_diff
from collections import deque
from typing import Sequence


def curses_menu(
    stdscr: curses.window,
    entries: Sequence[tuple[str, str]],
    title: str = "Select an entry",
) -> int:
    """Simply curses menu to select an entry from a list.

    Returns:
        The index of the selected entry.
    """
    curses.curs_set(0)  # Hide cursor
    current_row = 0

    def print_menu() -> None:
        entry_length = max(len(e[0]) for e in entries)
        line_length = entry_length + 2

        stdscr.clear()
        line = 0

        stdscr.addstr(line, 0, title)
        line += 1
        stdscr.addstr(line, 0, "=" * line_length)
        line += 1

        for idx, (entry_name, _) in enumerate(entries):
            if idx == current_row:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(line, 0, f" {entry_name:<{entry_length}} ")
                line += 1
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(line, 0, f" {entry_name}")
                line += 1

        stdscr.addstr(line, 0, "=" * line_length)
        line += 1
        stdscr.addstr(
            line,
            0,
            "Select: ↑/↓/j/k | Enter: Confirm | Q: quit",
        )
        line += 1

        line += 1  # add empty line
        stdscr.addstr(line, 0, "Selected entry's ID:")
        line += 1
        stdscr.addstr(
            line,
            0,
            entries[current_row][1],
        )
        line += 1

        stdscr.refresh()

    print_menu()
    while True:
        key = stdscr.getch()
        if key in (curses.KEY_UP, ord("k")) and current_row > 0:
            current_row -= 1
        elif key in (curses.KEY_DOWN, ord("j")) and current_row < len(entries) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return current_row
        elif key == ord("q"):
            raise KeyboardInterrupt
        print_menu()


def get_grub_entries(
    grub_cfg_path: str = "/boot/grub/grub.cfg",
) -> list[tuple[str, str]]:
    """Parse grub config to get all menu entries.

    Returns:
        List of tuples with the entry name and its ID.
    """
    entries = []
    submenu_stack: deque[tuple[str, str]] = deque()
    current_submenu = None

    with open(grub_cfg_path, "r") as grub_cfg:
        for line in grub_cfg:
            submenu_match = re.match(
                r"^\s*submenu '([^']+)'.* \$menuentry_id_option '([^']+)'", line
            )
            menuentry_match = re.match(
                r"^\s*menuentry '([^']+)'.* \$menuentry_id_option '([^']+)'", line
            )

            if submenu_match:
                # close previous submenu
                # TODO: This does currently not work correctly for nested submenus!
                if submenu_stack:
                    submenu_stack.pop()
                    current_submenu = submenu_stack[-1] if submenu_stack else None

                submenu_stack.append((submenu_match.group(1), submenu_match.group(2)))
                current_submenu = submenu_stack[-1]

            elif menuentry_match:
                entry_name = menuentry_match.group(1)
                entry_id = menuentry_match.group(2)
                if current_submenu:
                    full_id = f"{current_submenu[1]}>{entry_id}"
                else:
                    full_id = entry_id
                entries.append((entry_name, full_id))

    return entries


def update_grub_default(entry_id: str) -> None:
    """Update GRUB_DEFAULT in /etc/default/grub to the selected entry.

    First prints the diff to be applied and asks for confirmation before updating.
    """
    grub_default_path = "/etc/default/grub"
    with open(grub_default_path, "r") as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if line.startswith("GRUB_DEFAULT="):
            new_lines.append(f'GRUB_DEFAULT="{entry_id}"\n')
        else:
            new_lines.append(line)

    diff = unified_diff(lines, new_lines, fromfile="current", tofile="new")
    diff_output = "".join(diff)
    print()
    print(f"Diff to be applied to {grub_default_path}.  PLEASE REVIEW CAREFULLY!:\n")
    print("-" * 60)
    print(diff_output)
    print("-" * 60)

    confirm = input("Apply changes? (y/N): ").strip().lower()
    if confirm == "y":
        with open(grub_default_path, "w") as file:
            file.writelines(new_lines)
        print("GRUB configuration updated.  Please run `sudo update-grub`.")
    else:
        print("No changes applied.")


def main() -> None:  # noqa: D103
    # use argparse only for the help message
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--grub-cfg-path",
        default="/boot/grub/grub.cfg",
        help="Path to grub.cfg.  Default: %(default)s",
    )
    args = parser.parse_args()

    entries = get_grub_entries(args.grub_cfg_path)
    if not entries:
        print("No entries found in grub.cfg")
        return

    selected_index = curses.wrapper(
        curses_menu, entries, "Select the kernel to set as default:"
    )
    selected_entry_id = entries[selected_index][1]
    update_grub_default(selected_entry_id)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    except PermissionError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
