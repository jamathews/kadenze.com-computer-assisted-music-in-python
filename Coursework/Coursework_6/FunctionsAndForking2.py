from scamp import *

s = Session()
s.tempo = 80

sax = s.new_part("saxophone")
bass = s.new_part("pitched bass")


def sax_part():
    while True:
        sax.play_note(74, 0.7, 1.0)
        sax.play_note(73, 0.7, 1.0)
        sax.play_note(72, 0.7, 5/6)
        sax.play_note(70, 0.7, 0.5)
        sax.play_note(67, 0.7, 1/6)
        sax.play_note(66, 0.7, 1/3)
        sax.play_note(62, 0.7, 1/6)
        sax.play_note(64, 0.7, 1/3)
        sax.play_note(66, 0.7, 1/6)
        sax.play_note(67, 0.7, 1/3)
        sax.play_note(69, 0.7, 1/6)
        sax.play_note(70, 0.7, 1/3)
        sax.play_note(72, 0.7, 1/6)


def bass_part():
    while True:
        for pitch in [38, 32, 33, 39, 38, 44, 43]:
            bass.play_note(pitch, 0.7, 0.5)
        bass.play_note(37, 0.9, 0.5/3)
        bass.play_note(38, 0.9, 0.5/3)
        bass.play_note(39, 0.9, 0.5/3)
        

# Try all of the possibilities below, commenting out (command/ctrl-3)
# all of the others. What happens in each case? Why?
sax_part()
bass_part()


# bass_part()
# sax_part()


# fork(sax_part)
# bass_part()


# bass_part()
# fork(sax_part)


# fork(sax_part)
# fork(bass_part)


# fork(sax_part)
# fork(bass_part)
# wait_for_children_to_finish()