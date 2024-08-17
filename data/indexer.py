import os
import fnmatch
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


class Metadata:
    def __init__(self, file):
        self.audio = MP3(file, ID3=EasyID3)

    @property
    def title(self):
        return self.audio.get("title", ["Unknown Title"])[0]

    @property
    def artist(self):
        return self.audio.get("artist", ["Unknown Artist"])[0]

    @property
    def album(self):
        return self.audio.get("album", ["Unknown Album"])[0]

    @property
    def genre(self):
        return self.audio.get("genre", ["Unknown Genre"])[0]

    @property
    def track_number(self):
        return self.audio.get("tracknumber", ["Unknown Track"])[0]

    @property
    def date(self):
        return self.audio.get("date", ["Unknown Date"])[0]

    @property
    def duration(self):
        return int(self.audio.info.length) if self.audio.info else 0

    @property
    def bitrate(self):
        return self.audio.info.bitrate if self.audio.info else 0

    @property
    def sample_rate(self):
        return self.audio.info.sample_rate if self.audio.info else 0

    @property
    def channels(self):
        return self.audio.info.channels if self.audio.info else 0


def get_files(base_path, file_type="mp3"):
    result = []
    for root, dirs, files in os.walk(base_path):
        for name in files:
            if fnmatch.fnmatch(name, "*." + file_type):
                result.append(os.path.join(root, name))
    return result


print("run indexer")
file_type = "mp3"
base_path = "/home/cafalchio/Projects/music_player/data"

d = [Metadata(file) for file in get_files(base_path, file_type)]
