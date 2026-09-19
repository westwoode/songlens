class Song:
    def __init__(self, title, artist, album, year, sections = None):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        if sections is None:
            self.sections = []
        else:
            self.sections = sections

    def add_section(self, section):
        self.sections.append(section)

    def __str__(self):
        return f"{self.title} by {self.artist} from the album {self.album} ({self.year})"