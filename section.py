class Section:
    def __init__(self, title, lyrics = None):
        self.title = title
        if lyrics is None:
            self.lyrics = []
        else:
            self.lyrics = lyrics

    def __str__(self):
        return f"Section: {self.title}\n{self.lyrics}"