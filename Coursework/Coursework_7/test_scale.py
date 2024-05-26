from unittest import TestCase

from scale import Scale


class TestScale(TestCase):
    def setUp(self):
        self.tonic = 60
        self.scale = Scale(self.tonic)

    def test_note_none(self):
        self.assertRaises(ValueError, self.scale.note, None)

    def test_note_zero(self):
        self.assertRaises(ValueError, self.scale.note, 0)

    def test_note_positive_1(self):
        self.assertEqual(self.scale[1], self.tonic)

    def test_note_positive_7(self):
        # 7th scale degree of a major scale is 11 semitones
        self.assertEqual(self.scale[7], self.tonic + 11)

    def test_note_positive_octave(self):
        # octave is 12 semitones
        self.assertEqual(self.scale[8], self.tonic + 12)

    def test_note_positive_octave_fifth(self):
        # octave is 12 semitones, fifth is 7 semitones
        self.assertEqual(self.scale[12], self.tonic + 12 + 7)

    def test_note_negative_1(self):
        self.assertEqual(self.scale[-1], self.tonic)

    def test_note_negative_7(self):
        self.assertEqual(self.scale[-7], self.tonic - 10)

    def test_note_negative_octave(self):
        # octave is 12 semitones
        self.assertEqual(self.scale[-8], self.tonic - 12)

    def test_note_negative_octave_fifth(self):
        self.assertEqual(self.scale[-12], self.tonic - 12 - 7)
