from song import Song
from section import Section
from lyric_line import LyricLine

def main():
    song1 = Song("Song Title", "Artist Name", "Album Name", 2023)

    verse1 = Section("Verse 1")

    line1 = LyricLine("I am lost in the stars", 1)
    line2 = LyricLine("Searching for a place to belong", 2)

    verse1.add_line(line1)
    verse1.add_line(line2)

    song1.add_section(verse1)

    print(song1)

    for section in song1.sections:
        print(section.title)

        for line in section.lyrics:
            print(line)

if __name__ == "__main__":
    main()