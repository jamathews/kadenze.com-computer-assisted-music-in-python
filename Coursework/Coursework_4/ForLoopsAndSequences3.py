from scamp import *

s = Session()

piano = s.new_part("piano")
organ = s.new_part("organ")

for pitch in range(50, 67):
    if pitch > 62:
        piano.play_note(pitch, 0.7, 0.25)
    else:
        organ.play_note(pitch, 0.7, 0.25)
        organ.play_note(pitch + 4, 0.7, 0.25 / 2)
        organ.play_note(pitch + 7, 0.7, 0.25 / 2)

wait(1)

for pitch in range(50, 67):
    if pitch % 5 == 1:
        piano.play_note(pitch, 0.7, 0.25)
        piano.play_note(pitch - 5, 0.7, 0.125)
        piano.play_note(pitch - 8, 0.7, 0.125)
    else:
        organ.play_note(pitch, 0.7, 0.25)
    organ.play_note(pitch + 12, 0.7, 0.5, blocking=False)
    piano.play_note(pitch, 0.7, 0.25)
