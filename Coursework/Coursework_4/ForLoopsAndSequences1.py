from scamp import *

s = Session()

violin = s.new_part("violin")
viola = s.new_part("viola")
cello = s.new_part("cello")

for pitch in range(55, 80):
    print(f"{pitch} ", end="")
    violin.play_note(pitch, 0.7, 0.25)
print("\n")

wait(1)

for pitch in range(55, 80, 3):
    print(f"{pitch} ", end="")
    cello.play_note(pitch - 8 - 12, 0.7, 0.25, blocking=False)
    viola.play_note(pitch - 5, 0.7, 0.25, blocking=False)
    violin.play_note(pitch, 0.7, 0.25)
print("\n")

wait(1)

for pitch in [59, 66, 64, 54, 88, 60, 67, 65, 55, 89, 61, 68, 66, 56, 90]:
    print(f"{pitch} ", end="")
    viola.play_note(pitch, 0.7, 0.25)
print("\n")
