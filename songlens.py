from song import Song
from section import Section
from lyric_line import LyricLine
from interpretation import Interpretation

def main():
    song1 = Song("Song Title", "Artist Name", "Album Name", 2023)

    verse1 = Section("Verse 1")

    line1 = LyricLine("I am lost in the stars", 1)
    line1.add_interpretation(
        Interpretation(
            "Symbolism",
            "The stars represent hope and possibilities."
        )
    )

    line1.add_interpretation(
        Interpretation(
            "Emotional",
            "The speaker feels disconnected and uncertain about their future."
        )
    )

    line2 = LyricLine("Searching for a place to belong", 2)

    verse1.add_line(line1)
    verse1.add_line(line2)

    song1.add_section(verse1)

    print(song1)

    for section in song1.sections:
        print(section.title)

        for line in section.lyrics:
            print(line)

    print("\nInterpretations for:", line1.text)

    for interpretation in line1.interpretations:
        print("-", interpretation)

if __name__ == "__main__":
    main()