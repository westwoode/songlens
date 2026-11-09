import unittest

from song import Song
from section import Section
from lyric_line import LyricLine
from interpretation import Interpretation
import os
import tempfile
from storage import save_song, load_song


class TestSongLens(unittest.TestCase):

    def test_song_creation(self):
        song = Song("Test Song", "Test Artist", "Test Album", 2026)

        self.assertEqual(song.title, "Test Song")
        self.assertEqual(song.artist, "Test Artist")
        self.assertEqual(song.sections, [])

    def test_add_section(self):
        song = Song("Test Song", "Test Artist", "Test Album", 2026)
        verse = Section("Verse 1")

        song.add_section(verse)

        self.assertEqual(len(song.sections), 1)
        self.assertIs(song.sections[0], verse)

    def test_add_lyric(self):
        verse = Section("Verse 1")
        lyric = LyricLine("I am lost in the stars", 1)

        verse.add_line(lyric)

        self.assertEqual(len(verse.lyrics), 1)
        self.assertIs(verse.lyrics[0], lyric)

    def test_multiple_interpretations(self):
        lyric = LyricLine("I am lost in the stars", 1)

        lyric.add_interpretation(
            Interpretation("Symbolism", "Stars represent hope.")
        )

        lyric.add_interpretation(
            Interpretation("Emotional", "The speaker feels lost.")
        )

        self.assertEqual(len(lyric.interpretations), 2)
        self.assertEqual(
            lyric.interpretations[0].category,
            "Symbolism"
        )

    def test_lyrics_have_independent_interpretations(self):
        line1 = LyricLine("First lyric", 1)
        line2 = LyricLine("Second lyric", 2)

        line1.add_interpretation(
            Interpretation("Symbolism", "Represents hope.")
        )

        self.assertEqual(len(line1.interpretations), 1)
        self.assertEqual(len(line2.interpretations), 0)

    def test_sections_have_independent_lyrics(self):
        verse1 = Section("Verse 1")
        verse2 = Section("Verse 2")

        verse1.add_line(LyricLine("First lyric", 1))

        self.assertEqual(len(verse1.lyrics), 1)
        self.assertEqual(len(verse2.lyrics), 0)

    def test_save_and_load_song(self):
        song = Song("Test Song", "Test Artist", "Test Album", 2026)

        verse = Section("Verse 1")
        lyric = LyricLine("I am lost in the stars", 1)

        lyric.add_interpretation(
            Interpretation("Symbolism", "Stars represent hope.")
        )

        verse.add_line(lyric)
        song.add_section(verse)

        with tempfile.TemporaryDirectory() as directory:
            filename = os.path.join(directory, "test_song.json")

            save_song(song, filename)
            loaded_song = load_song(filename)

        self.assertEqual(song.to_dict(), loaded_song.to_dict())

        self.assertIsInstance(loaded_song, Song)
        self.assertIsInstance(loaded_song.sections[0], Section)
        self.assertIsInstance(
            loaded_song.sections[0].lyrics[0],
            LyricLine
        )
        self.assertIsInstance(
            loaded_song.sections[0].lyrics[0].interpretations[0],
            Interpretation
        )


if __name__ == "__main__":
    unittest.main()