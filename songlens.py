import song
import section

def main():
    song1 = song.Song("Song Title", "Artist Name", "Album Name", 2023)
    section1 = section.Section("Verse 1", ["Line 1", "Line 2"])
    song1.add_section(section1)
    print(song1)

    for section in song1.sections:
        print(section)

main()