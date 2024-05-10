from scamp import *

s = Session(default_soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")

s.tempo = 72

# s.print_default_soundfont_presets()

drum_kit = s.new_part("Kit 1")

x = 7
while x > 0:
    print(x)
    drum_kit.play_note(66, 0.5, 0.25)
    x -= 1

print("Go!")

while True:
    drum_kit.play_note(60, 1.0, 0.5, blocking=False)
    drum_kit.play_note(70, 1.0, 0.5)
    drum_kit.play_note(66, 0.5, 0.5)
    wait(0.25)
    drum_kit.play_note(58, 0.5, 0.25)
    drum_kit.play_note(66, 0.5, 0.5)

