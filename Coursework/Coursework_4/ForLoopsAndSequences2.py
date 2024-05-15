from scamp import *

s = Session()

piano = s.new_part("piano")

for pitch in range(60, 72):
    piano.play_note(pitch, 0.7, 0.125)
    piano.play_note(pitch - 5, 0.7, 0.125)

for pitch in [60, 67, 63, 56, 89, 77, 65]:
    piano.play_note(pitch, 0.7, 0.1)
    piano.play_note(pitch + 1, 0.7, 0.1)
    piano.play_note(pitch - 1, 0.7, 0.1)
