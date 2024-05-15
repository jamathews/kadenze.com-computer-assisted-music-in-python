from scamp import *

s = Session()

piano = s.new_part("piano")

for pitch in range(60, 72):
    piano.play_note(pitch, 0.7, 0.125)
    piano.play_note(pitch - 8, 0.7, 0.125 * 2)
    piano.play_note(pitch // 2, 0.7, 0.125)

for pitch in [60, 67, 63, 56, 89, 77, 65]:
    piano.play_note(pitch, 0.7, 0.1 * 3)
    piano.play_note(pitch + 13, 0.7, 0.1)
    piano.play_note(pitch - 13, 0.7, 0.1 * 2)
    piano.play_note(pitch * 2 - 24, 0.7, 0.1)
