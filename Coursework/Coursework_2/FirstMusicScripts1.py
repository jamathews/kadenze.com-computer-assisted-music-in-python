from scamp import *

s = Session()

clar = s.new_part("Clarinet")

clar.play_note(60, 0.5, 2.0)