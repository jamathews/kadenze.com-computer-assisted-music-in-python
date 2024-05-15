from scamp import *

s = Session()

violin = s.new_part("violin")

for p in range(55, 80):
    violin.play_note(p, 0.7, 0.25)

wait(1)

for p in range(55, 80, 3):
    violin.play_note(p, 0.7, 0.25)

wait(1)

for p in [60, 67, 65, 55, 89]:
    violin.play_note(p, 0.7, 0.25)
