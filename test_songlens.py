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

    def test_empty_lyric_rejected(self):
        with self.assertRaises(ValueError):
            LyricLine("   ", 1)

    def test_invalid_line_number_rejected(self):
        with self.assertRaises(ValueError):
            LyricLine("Valid lyric", -3)

        with self.assertRaises(ValueError):
            LyricLine("Valid lyric", True)

    def test_empty_song_title_rejected(self):
        with self.assertRaises(ValueError):
            Song("", "Artist", "Album", 2026)

    def test_empty_artist_rejected(self):
        with self.assertRaises(ValueError):
            Song("Title", "   ", "Album", 2026)

    def test_invalid_song_year_rejected(self):
        with self.assertRaises(ValueError):
            Song("Title", "Artist", "Album", "2026")

        with self.assertRaises(ValueError):
            Song("Title", "Artist", "Album", True)

    def test_empty_section_title_rejected(self):
        with self.assertRaises(ValueError):
            Section("   ")

    def test_invalid_lyric_rejected(self):
        verse = Section("Verse 1")

        with self.assertRaises(TypeError):
            verse.add_line("This is just a string")

    def test_invalid_initial_lyrics_rejected(self):
        with self.assertRaises(TypeError):
            Section("Verse 1", ["Line 1", "Line 2"])

    def test_empty_interpretation_category_rejected(self):
        with self.assertRaises(ValueError):
            Interpretation("", "A valid explanation.")

    def test_empty_interpretation_explanation_rejected(self):
        with self.assertRaises(ValueError):
            Interpretation("Symbolism", "   ")

    def test_invalid_interpretation_source_rejected(self):
        with self.assertRaises(TypeError):
            Interpretation("Symbolism", "Represents hope.", 123)

    def test_invalid_section_rejected(self):
        song = Song("Title", "Artist", "Album", 2026)

        with self.assertRaises(TypeError):
            song.add_section("Verse 1")

    def test_invalid_initial_sections_rejected(self):
        with self.assertRaises(TypeError):
            Song("Title", "Artist", "Album", 2026, ["Verse 1"])

    def test_invalid_interpretation_rejected(self):
        lyric = LyricLine("First lyric", 1)

        with self.assertRaises(TypeError):
            lyric.add_interpretation("Some interpretation")

    def test_invalid_initial_interpretations_rejected(self):
        with self.assertRaises(TypeError):
            LyricLine("First lyric", 1, ["Some interpretation"])

    def test_load_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            filename = os.path.join(directory, "missing_song.json")

            with self.assertRaisesRegex(
                FileNotFoundError,
                "Song file not found"
            ):
                load_song(filename)

if __name__ == "__main__":
    unittest.main()