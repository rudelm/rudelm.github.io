#!/usr/bin/env python3
from pathlib import Path
import os
import re

content_dir = 'static/wp-content/uploads'

def delete_file(file_entry):
    if os.path.exists(file_entry):
        os.remove(file_entry)
    else:
        print("Can not delete {} as it doesn't exists".format(file_entry))

for root, dirs, files in os.walk(content_dir):
    for file in files:
        result = re.search(r"(.*)-(\d{3}x\d{3})|(.thumbnail).*", file)
        if result:
            delete_file(os.path.join(root, file))