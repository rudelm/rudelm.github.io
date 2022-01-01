#!/usr/bin/env python3
from pathlib import Path
import os
import re
import shutil

content_dir = 'content/post'
it = os.scandir(content_dir)

def move_to_dir(file_entry, result):
    year = result.group(1)
    month = result.group(2)
    day = result.group(3)
    title = result.group(4)
    new_path = "{}/{}/{}/{}/{}/".format(content_dir, year, month, day, title)
    create_dir(new_path)
    move_post(new_path, title, file_entry)

def create_dir(target_path):
    if not os.path.exists(target_path):
        print("Will create: {}".format(target_path))
        path = Path(target_path)
        path.mkdir(parents=True, exist_ok=True)
    else:
        return

def move_post(target_path, title, file_entry):
    old_post_path = Path(file_entry)
    new_post_path = Path("{}/{}.md".format(target_path, title))
    if not os.path.exists(new_post_path):
        shutil.move(old_post_path, new_post_path)
        print("Moved posts to {}".format(new_post_path))
    else:
        return


for entry in it:
    if entry.name.endswith('.md'):
        # its a markdown file we can scan for parts
        result = re.search(r"(\d{4})-(\d{2})-(\d{2})-(.*).md", entry.name)
        move_to_dir(entry, result)
        