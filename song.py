from section import Section

class Song:
    def __init__(self, title, artist, album, year, sections = None):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Song title must be a non-empty string.")

        if not isinstance(artist, str) or not artist.strip():
            raise ValueError("Artist name must be a non-empty string.")

        if not isinstance(album, str) or not album.strip():
            raise ValueError("Album name must be a non-empty string.")

        if type(year) is not int or year < 1000 or year > 9999:
            raise ValueError("Year must be a four-digit integer.")

        self.title = title
        self.artist = artist
        self.album = album
        self.year = year

        if sections is None:
            sections = []

        if not isinstance(sections, list):
            raise TypeError("Sections must be a list.")

        if not all(isinstance(section, Section) for section in sections):
            raise TypeError("All sections must be Section objects.")

        self.sections = sections

    def add_section(self, section):
        if not isinstance(section, Section):
            raise TypeError("Only Section objects can be added.")

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

    @classmethod
    def from_dict(cls, data):
        from section import Section

        sections = [
            Section.from_dict(item)
            for item in data["sections"]
        ]

        return cls(
            data["title"],
            data["artist"],
            data["album"],
            data["year"],
            sections
        )