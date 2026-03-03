# write_files.py

from pathlib import Path

# Создание файла и запись данных
file_path = Path("sample.txt")

with file_path.open("w") as file:
    file.write("Hello, Python!\n")
    file.write("This is Practice 6.\n")

print("File created and data written.")

# Append data
with file_path.open("a") as file:
    file.write("This line was appended.\n")

print("New line appended.")