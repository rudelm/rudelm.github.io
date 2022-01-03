#!/usr/bin/env python3
from pathlib import Path
import os
import re

content_dir = 'static/wp-content/uploads'
post_dir = 'content/post'
unused_files=set()
used_files=set()
all_image_files={}

def delete_file(file_entry):
    if os.path.exists(file_entry):
        os.remove(file_entry)
        print("Removed file successfully: {}".format(file_entry))
    else:
        print("Can not delete {} as it doesn't exists".format(file_entry))

def remove_thumbnails(root, file):
    result = re.search(r"(.*)-(\d{1,4}x\d{1,4})|(.thumbnail).*", file)
    if result:
        delete_file(os.path.join(root, file))

def move_to_posts(root, file):
    result = re.search(r"(.*)(\d{4})\/(\d{2})", root)
    if result:
        year = result.group(2)
        month = result.group(3)
        print("root {}, file {}".format(root, file))

def check_usage_in_post():
    for post_root, post_dirs, post_files in os.walk(post_dir):
        for post_file in post_files:
            checked_post_file = os.path.join(post_root, post_file)
            for image_file, image_path in all_image_files.items():
                checked_file = os.path.join(post_root, post_file)
                with open(checked_file) as f:
                    # we should only check for the base filename, as converted blog posts might still reference the thumbnailed versions
                    # ideally we would check here for the base filename plus anything in between and the file type
                    file_content = f.read()
                    matches = re.findall("", file_content)
                    if matches:
                        print("{} is still in use in post {}".format(image_file, checked_post_file))
                        used_files.add(image_file)

def create_unused_files():
    # all_image_files minus used_files should give the list of unused_files
    for image_file, image_path in all_image_files.items():
        if image_file not in used_files:
            unused_files.add(image_path)


for root, dirs, files in os.walk(content_dir):
    for file in files:
        current_file = os.path.join(root, file)
        remove_thumbnails(root, file)
        all_image_files[file] = current_file

check_usage_in_post()
create_unused_files()
#move_to_posts(root, file)
print("Found {} files, in use were only {}".format(len(all_image_files), len(used_files)))
print("Found {} unused files that will be deleted".format(len(unused_files)))

for file in unused_files:
    delete_file(file)