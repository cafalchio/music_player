import json
from glob import glob
import os

SOURCE_FOLDER = os.path.expanduser("~/portainer/downloads/lidarr")  # Expand the tilde to full path
MUSIC_FILE = './musics.json'

def get_local_library():
    if os.path.isfile(MUSIC_FILE):
        print("Found file")
        with open(MUSIC_FILE, "r") as f:
            files = json.load(f)
            print(files)
        return files
    else:
        print("Looking for files")
        files = glob(os.path.join(SOURCE_FOLDER, '**', '*.mp3'), recursive=True)
        with open(MUSIC_FILE, 'w', encoding='utf-8') as f:
            print("Writing files to music.json")
            json.dump(files, f, ensure_ascii=False, indent=4)
    return files

# Example usage
files = get_local_library()
print(files)
