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