from scamp import *

s = Session()

piano = s.new_part("piano")
organ = s.new_part("organ")

for pitch in range(50, 67):
    if pitch < 58:
        piano.play_note(pitch, 0.7, 0.25)
    else:
        organ.play_note(pitch, 0.7, 0.25)

wait(1)

for pitch in range(50, 67):
    if pitch % 2 == 0:
        piano.play_note(pitch, 0.7, 0.25)
    else:
        organ.play_note(pitch, 0.7, 0.25)