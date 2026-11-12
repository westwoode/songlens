import json
from song import Song


def save_song(song, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(song.to_dict(), file, indent=4)

def load_song(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"Song file not found: {filename}"
        ) from error

    return Song.from_dict(data)