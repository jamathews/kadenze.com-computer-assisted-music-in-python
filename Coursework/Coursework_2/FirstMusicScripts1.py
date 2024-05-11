import random

from scamp import *

s = Session()
kit_session = Session(default_soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
s.tempo = 90
kit_session.tempo = s.tempo

violin = s.new_part("Pizzicato Violin")
viola = s.new_part("Viola")
cello = s.new_part("Cello")
bass = s.new_part("String Bass")
tuba = s.new_part("Tuba")
drums = kit_session.new_part("Kit 1")

position = 0
pitch = 80
length = 0.5
volume = 0.5
trend_down = (0.95, 1)
trend_up = (1, 1.05)
trend = random.choice([trend_up, trend_down])
duration = random.randint(75, 120)


def update_note():
    global trend, pitch, volume, length
    if position > duration * 0.9:
        trend = trend_up
    elif pitch > 90:
        trend = trend_down
    elif pitch < 40:
        trend = trend_up
    else:
        trend = random.choice([trend_up, trend_down])
    pitch = random.uniform(pitch * trend[0], pitch * trend[1])
    volume = random.uniform(volume * trend[0] ** 2, volume * trend[1] ** 2)
    length = random.uniform(length * trend[0], length * trend[1])
    print(f"{position=}/{duration}, {trend=}, {pitch=}, {volume=}, {length=}")


def play():
    global position
    for i in range(4):
        play_drums()
    for _ in range(duration):
        position += 1

        play_drums()

        update_note()
        viola.play_note(pitch, volume, length, blocking=True)

        if random.choice([True, False]):
            update_note()
            violin.play_note(pitch / 4 * 3, volume, length, blocking=False)

        if position % 2 == 0:
            update_note()
            cello.play_note(pitch * 3 / 4, volume, length / 2, blocking=False)

        if position % 3 == 0:
            update_note()
            bass.play_note(pitch * 2 / 3, volume, length * 1.5, blocking=False)

        if position % 4 == 0:
            tuba.play_note(pitch * 1 / 2, 0.8, 1 / 4, blocking=False)
        elif position % 4 == 2:
            tuba.play_note(pitch * 1 / 3, 0.5, 1 / 8, blocking=False)
    else:
        update_note()
        viola.play_note(pitch, volume, 1, blocking=True)
        viola.play_note(pitch, volume, 1, blocking=True)
        update_note()
        viola.play_note(pitch, volume, 1, blocking=True)
        update_note()
        viola.play_note(pitch, volume, 4, blocking=True)


def play_drums():
    global position
    drums.play_note(random.choice([42, 44, 46]), volume / 4, length / 2, blocking=True)
    drums.play_note(random.choice([42, 44, 46]), volume / 4, length / 2, blocking=True)
    drums.play_note(random.choice([42, 44, 46]), volume / 4, length * 2, blocking=False)
    if position % 4 == 0 or position % 4 == 2:
        drums.play_note(35, 1, length, blocking=False)
    elif position % 4 == 1:
        drums.play_note(37, 1, length, blocking=False)
    elif position % 4 == 3:
        toms = random.choices([41, 43, 45, 47, 48, 50], k=2)
        toms.sort()
        drums.play_note(toms[1], 1 / 8, length / 2, blocking=True)
        drums.play_note(toms[0], 1 / 8, length / 2, blocking=False)


if __name__ == '__main__':
    play()
