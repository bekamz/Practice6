# read_files.py

from pathlib import Path

file_path = Path("sample.txt")

# read()
with file_path.open("r") as file:
    content = file.read()
    print("Using read():")
    print(content)

# readline()
with file_path.open("r") as file:
    print("Using readline():")
    print(file.readline())

# readlines()
with file_path.open("r") as file:
    print("Using readlines():")
    print(file.readlines())