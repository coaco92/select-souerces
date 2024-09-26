#!/usr/bin/env python3
import os
import re


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
    print("请选择一个备份文件：")
    for i, name in enumerate(backup_files, start=1):
        print(f"{i}. {name}")


def get_user_choice(backup_files):
    while True:
        try:
            choice = input("请输入数字选择或 q 退出：")
            if choice.lower() == "q":
                return None
            choice = int(choice)
            if 1 <= choice <= len(backup_files):
                return choice - 1
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请输入一个数字或 q 退出。")


def create_symlink(sources_dir, selected_backup):
    target = os.path.join(sources_dir, f"sources.list.{selected_backup}")
    link = os.path.join(sources_dir, "sources.list")

    if os.path.islink(link):
        os.remove(link)

    os.symlink(target, link)
    print(f"已将 {target} 设置为新的 sources.list")


def show_sources_list_with_cat(sources_dir):
    link = os.path.join(sources_dir, "sources.list")
    subprocess.run(["cat", link])


def main():
    sources_dir = "/etc/apt/"
    backup_files = list_sources_backups()

    if not backup_files:
        print("没有找到任何 sources.list 备份文件。")
        return

    display_options(backup_files)
    choice = get_user_choice(backup_files)
    if choice is None:
        return

    selected_backup = backup_files[choice]
    create_symlink(sources_dir, selected_backup)

    show_sources_list_with_cat(sources_dir)


if __name__ == "__main__":
    main()
