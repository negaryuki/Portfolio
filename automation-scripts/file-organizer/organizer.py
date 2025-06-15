### 🐍 `organizer.py`

```python




import os                        #os: Provides a way to interact with the operating system.
import shutil                    #shutil: Used for high-level file operations like copying or moving files.
import sys                       #sys: Lets us access command-line arguments.
from pathlib import Path         #pathlib.Path: Modern, object-oriented way to work with file paths.

# Map file types to folders
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
    'Others': []
}


# Takes a file extension like .jpg as input
# looks for FILE_TYPES
# if found it returns the catergorym else 'it defaults to 'Others'
def get_category(file_ext):
    for category, extensions in FILE_TYPES.items():
        if file_ext.lower() in extensions:
            return category
    return 'Others'


# Converts the input path to a PATH Object
# Check if the path is a valid folder

def organize_folder(path):
    path = Path(path)
    if not path.is_dir():
        print(f"❌ Error: {path} is not a valid folder path.")
        return

    for item in path.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            target_folder = path / category
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_folder / item.name))
            print(f"✅ Moved: {item.name} → {category}/")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python organizer.py /path/to/folder")
    else:
        folder_path = sys.argv[1]
        organize_folder(folder_path)
