#!/usr/bin/env python3
import os
import re
import subprocess


def list_sources_backups():
    backup_files = []
    sources_dir = "/etc/apt/"

    for filename in os.listdir(sources_dir):
        if filename.startswith("sources.list.") and os.path.isfile(
            os.path.join(sources_dir, filename)
        ):
            match = re.match(r"sources\.list\.(.+)", filename)
            if match:
                backup_files.append(match.group(1))

    return backup_files


def display_options(backup_files):
    print("Please select a backup file:")
    for i, name in enumerate(backup_files, start=1):
        print(f"{i}. {name}")
    print("! to directly view the current sources.list file")
    print("q to quit")


def get_user_choice(backup_files):
    while True:
        choice = input("Enter a number or q to quit: ")
        if choice.lower() == "q":
            return None
        elif choice == "!":
            return "!"
        try:
            choice = int(choice)
            if 1 <= choice <= len(backup_files):
                return choice - 1
            else:
                print("Invalid choice, please enter again.")
        except ValueError:
            print("Invalid input, please enter a number or q to quit.")


def create_symlink(sources_dir, selected_backup):
    target = os.path.join(sources_dir, f"sources.list.{selected_backup}")
    link = os.path.join(sources_dir, "sources.list")

    if os.path.islink(link):
        os.remove(link)

    os.symlink(target, link)
    print(f"Set {target} as the new sources.list")


def show_sources_list_with_cat(sources_dir):
    link = os.path.join(sources_dir, "sources.list")
    if os.path.exists(link):
        try:
            subprocess.run(["cat", link], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Unable to display file {link}: {e}")
    else:
        print(f"File {link} does not exist.")


def main():
    sources_dir = "/etc/apt/"
    backup_files = list_sources_backups()

    if not backup_files:
        print("No sources.list backup files found.")
        return

    display_options(backup_files)
    choice = get_user_choice(backup_files)
    if choice is None:
        return

    if choice == "!":
        show_sources_list_with_cat(sources_dir)
    else:
        selected_backup = backup_files[choice]
        create_symlink(sources_dir, selected_backup)
        show_sources_list_with_cat(sources_dir)


if __name__ == "__main__":
    main()
