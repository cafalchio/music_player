import json
from glob import glob
import os

SOURCE_FOLDER = os.path.expanduser("/portainer/downloads/lidarr/**/")  # Expand the tilde to full path
MUSIC_FILE = 'musics.json'

def get_local_library():
    if os.path.isfile(MUSIC_FILE):
        with open(MUSIC_FILE, "r") as f:
            files = json.load(f)
        return files
    else:
        # Use **/*.mp3 to look for .mp3 files in all subfolders recursively
        files = glob(os.path.join(SOURCE_FOLDER, '*.mp3'), recursive=True)
        with open(MUSIC_FILE, 'w', encoding='utf-8') as f:
            json.dump(files, f, ensure_ascii=False, indent=4)
    return files

# Example usage
files = get_local_library()
print(files)
