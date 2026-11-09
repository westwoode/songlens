from lyric_line import LyricLine


class Section:
    def __init__(self, title, lyrics=None):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Section title must be a non-empty string.")

        if lyrics is None:
            lyrics = []

        if not isinstance(lyrics, list):
            raise TypeError("Lyrics must be a list.")

        if not all(isinstance(line, LyricLine) for line in lyrics):
            raise TypeError("All lyrics must be LyricLine objects.")

        self.title = title
        self.lyrics = lyrics

    def add_line(self, line):
        if not isinstance(line, LyricLine):
            raise TypeError("Only LyricLine objects can be added.")

        self.lyrics.append(line)

    def __str__(self):
        lines = "\n".join(str(line) for line in self.lyrics)
        return f"Section: {self.title}\n{lines}"

    def to_dict(self):
        return {
            "title": self.title,
            "lyrics": [
                line.to_dict()
                for line in self.lyrics
            ]
        }

    @classmethod
    def from_dict(cls, data):
        lyrics = [
            LyricLine.from_dict(item)
            for item in data["lyrics"]
        ]

        return cls(data["title"], lyrics)