import random
from random import choice

from scamp import *

s = Session(default_soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")

s.tempo = 72

s.print_default_soundfont_presets()

drum_kit = s.new_part("Kit 4")
bass = s.new_part("Bass Hit 1")

while True:
    x = 7
    while x > 0:
        print(x)
        bass.play_note(choice([60, 61]), 0.5, 0.5, blocking=False)
        drum_kit.play_note(66, 0.5, 0.25)
        x -= 1

    print("Go!")

    for _ in range(random.randint(2, 12)):
        bass.play_note(50, 0.25, 1.0, blocking=False)
        drum_kit.play_note(60, 1.0, 0.5, blocking=False)
        drum_kit.play_note(70, 1.0, 0.5)
        bass.play_note(55, 0.25, 0.5, blocking=False)
        drum_kit.play_note(66, 0.5, 0.5)
        bass.play_note(73, 0.25, 0.25, blocking=False)
        wait(0.25)
        bass.play_note(choice([74, 75]), 0.25, 0.75, blocking=False)
        drum_kit.play_note(58, 0.5, 0.25)
        drum_kit.play_note(66, 0.5, 0.5)
