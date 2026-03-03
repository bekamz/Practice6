# create_list_dirs.py

import os
from pathlib import Path

# Create nested directories
Path("test_dir/sub_dir").mkdir(parents=True, exist_ok=True)
print("Directories created.")

# List files and folders
print("Contents of current directory:")
print(os.listdir())

# Current working directory
print("Current directory:", os.getcwd())