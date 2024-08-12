import json
from glob import glob
import os

SOURCE_FOLDER = os.path.expanduser("~/portainer/downloads/lidarr")  # Expand the tilde to full path
MUSIC_FILE = './musics.json'

def get_local_library():
    if os.path.isfile(MUSIC_FILE):
        print("Found file")
        try:
            with open(MUSIC_FILE, "r", encoding='utf-8') as f:
                files = json.load(f)
                # Check if the loaded files are indeed a list
                if isinstance(files, list):
                    return files
                else:
                    print("JSON file is not a list, recreating it.")
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error reading JSON file: {e}, recreating the file.")

    print("Looking for files")
    files = glob(os.path.join(SOURCE_FOLDER, '**', '*.mp3'), recursive=True)

    # Check if any files were found before writing to the JSON file
    if files:
        with open(MUSIC_FILE, 'w', encoding='utf-8') as f:
            print("Writing files to music.json")
            json.dump(files, f, ensure_ascii=False, indent=4)
    else:
        print("No MP3 files found.")

    return files

# Example usage
files = get_local_library()
print("Files found:", files)