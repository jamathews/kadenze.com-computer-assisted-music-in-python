from scamp import *

s = Session()
s.tempo = 76

oboe = s.new_part("oboe")
viola = s.new_part("viola")


def oboe_gesture():
    oboe.play_note(72, 0.9, 0.125)
    oboe.play_note(79, 0.9, 0.125)
    oboe.play_note(78, 0.6, 0.75)
    

def viola_gesture():
    for pitch in range(52, 58):
        viola.play_note(pitch, 0.7, 0.5/3)
        viola.play_note(pitch + 5, 0.7, 0.5/3)
        

oboe_gesture()
viola_gesture()
oboe_gesture()
