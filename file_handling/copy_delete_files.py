# copy_delete_files.py

import shutil
from pathlib import Path

source = Path("sample.txt")
backup = Path("sample_backup.txt")

# Copy file
shutil.copy(source, backup)
print("File copied successfully.")

# Delete file safely
if backup.exists():
    backup.unlink()
    print("Backup file deleted.")

# Find all .txt files
for file in Path(".").rglob("*.txt"):
    print("Found txt file:", file)