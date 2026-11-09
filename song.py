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

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "year": self.year,
            "sections": [
                section.to_dict()
                for section in self.sections
            ]
        }