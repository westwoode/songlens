class Section:
    def __init__(self, title, lyrics = None):
        self.title = title
        if lyrics is None:
            self.lyrics = []
        else:
            self.lyrics = lyrics

    def add_line(self, line):
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
        from lyric_line import LyricLine

        lyrics = [
            LyricLine.from_dict(item)
            for item in data["lyrics"]
        ]

        return cls(data["title"], lyrics)