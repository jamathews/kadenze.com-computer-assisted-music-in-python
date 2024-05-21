from datetime import datetime
from random import choice
from random import choices
from random import randint
from random import random
from random import uniform

from scamp import *

from scale import Scale

MAX_TEMPO = 90
MIN_TEMPO = 60

REPS = 4
SECTION_A_REPS = 8
SECTION_B_REPS = 4

ACOUSTIC_SNARE = 38
ELECTRIC_SNARE = 40
HAND_CLAP = 39
SNARES = [ACOUSTIC_SNARE, ELECTRIC_SNARE, HAND_CLAP]

ACOUSTIC_BASS_DRUM = 35
BASS_DRUM = 36
KICKS = [ACOUSTIC_BASS_DRUM, BASS_DRUM]

CLOSED_HAT = 42
OPEN_HAT = 46
PEDAL_HAT = 44
HATS = [CLOSED_HAT, OPEN_HAT, PEDAL_HAT]

CRASH_1 = 49
CRASH_2 = 57
CHINESE_CYMBAL = 52
SPLASH_CYMBAL = 55
CRASHES = [CRASH_1, CRASH_2, CHINESE_CYMBAL, SPLASH_CYMBAL]

RIDE_1 = 51
RIDE_BELL = 53
RIDE_2 = 59
RIDES = [RIDE_1, RIDE_BELL, RIDE_2]

DRUM_KITS_I_LIKE = [2, 3, 5, 8, 9]
SCRATCH_KITS_I_LIKE = [1, 2, 7, 9, 10, 13, 17]


def get_session(tempo=120, name=None) -> Session:
    if name:
        playback_settings.recording_file_path = name
    s = Session()
    s.tempo = tempo
    return s


def kick() -> int:
    return choice(KICKS)


def hat() -> int:
    return choice(HATS)


def snare() -> int:
    return choice(SNARES)


def crash() -> int:
    return choice(CRASHES)


def ride() -> int:
    return choice(RIDES)


def setup(new_parts):
    if new_parts:
        parts_list = "_".join([part["name"] for part in new_parts.values()])
        tempo = int(uniform(MIN_TEMPO, MAX_TEMPO))
        filename = f"{datetime.now().isoformat()}_{parts_list}_{tempo}BPM.wav"
        main_session = get_session(tempo, filename)
        # print_session_info(main_session)
        for key, val in new_parts.items():
            name = new_parts[key]["name"]
            soundfont = new_parts[key]["soundfont"]
            part = main_session.new_part(name, soundfont=soundfont)
            new_parts[key]["part"] = part
        return main_session


def intro(parts):
    print(f"\rIntro", end="")
    drum_kit = parts["drum_kit"]["part"]
    scratch = parts["scratch"]["part"]
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    scratch.play_note(48, 1 / 8, 2)

    wait(1)

    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    scratch.play_note(48, 1 / 8, 2)

    print(f" 1", end="")
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    scratch.play_note(60, 1 / 8, 1 / 4)
    scratch.play_note(62, 2 / 8, 1 / 4)
    scratch.play_note(64, 3 / 8, 1 / 4)
    scratch.play_note(65, 4 / 8, 1 / 4)

    print(f" 2", end="")
    scratch.play_note(67, 5 / 8, 1 / 4)
    scratch.play_note(69, 6 / 8, 1 / 4)
    scratch.play_note(71, 7 / 8, 1 / 4)
    scratch.play_note(72, 8 / 8, 1 / 4)

    print(f" 3", end="")
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    scratch.play_note(72, 1 / 8, 1 / 4)
    scratch.play_note(74, 2 / 8, 1 / 4)
    scratch.play_note(76, 3 / 8, 1 / 4)
    scratch.play_note(77, 4 / 8, 1 / 4)

    print(f" 4", end="")
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    scratch.play_note(79, 5 / 8, 1 / 4)
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    scratch.play_note(81, 6 / 8, 1 / 4)
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    scratch.play_note(83, 7 / 8, 1 / 4)
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    scratch.play_note(84, 8 / 8, 1 / 4)


def section_a(parts):
    print(f"\rSection A", end="")
    drum_kit = parts["drum_kit"]["part"]
    bass = parts["bass"]["part"]
    scratch = parts["scratch"]["part"]

    print(f" 1", end="")
    bass.play_note(48, 1 / 8, 1, blocking=False)
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)
    drum_kit.play_note(hat(), 3 / 4, 1 / 4)

    print(f" 2", end="")
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(kick(), 1 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)
    drum_kit.play_note(hat(), 3 / 4, 1 / 4)

    print(f" 3", end="")
    drum_kit.play_note(kick(), 2 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)
    bass.play_note(48, 1 / 8, uniform(1 / 8, 3 / 8), blocking=False)
    if choice([True, False]):
        drum_kit.play_note(snare(), 3 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(hat(), 3 / 4, 1 / 4)

    print(f" 4", end="")
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(kick(), 1 / 4, 1 / 4, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(72, 1 / 8, 1 / 4, blocking=False)
    drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)

    bass.play_note(46, 1 / 8, 1 / 4, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(snare(), 3 / 4, 1 / 4, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(kick(), 3 / 4, 1 / 2, blocking=False)
    if choice([True, False]):
        scratch.play_note(84, 1 / 8, 3 / 4, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(hat(), 3 / 4, 1 / 4)


def section_b(parts):
    print(f"\rSection B", end="")
    drum_kit = parts["drum_kit"]["part"]
    bass = parts["bass"]["part"]
    scratch = parts["scratch"]["part"]

    print(f" 1", end="")
    bass.play_note(60, 1 / 8, uniform(3 / 4, 1), blocking=False)
    drum_kit.play_note(kick(), 2 / 4, 1, blocking=False)
    drum_kit.play_note(OPEN_HAT, 3 / 4, 1 / 2, blocking=False)
    scratch.play_note(72, 8 / 8, 1 / 4, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)

    print(f" 2", end="")
    scratch.play_note(72, 8 / 8, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    bass.play_note(59, 1 / 8, uniform(1 / 4, 3 / 4), blocking=False)
    drum_kit.play_note(kick(), 2 / 4, 1, blocking=False)
    scratch.play_note(75, 8 / 8, 1 / 4, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    print(f" 3", end="")
    drum_kit.play_note(hat(), 3 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    bass.play_note(58, 1 / 8, uniform(3 / 8, 5 / 8), blocking=False)
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    scratch.play_note(72, 8 / 8, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)

    print(f" 4", end="")
    bass.play_note(57, 1 / 8, uniform(3 / 8, 5 / 8), blocking=False)
    drum_kit.play_note(kick(), 2 / 4, 1, blocking=False)
    drum_kit.play_note(crash(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    bass.play_note(56, 1 / 8, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    scratch.play_note(78, 8 / 8, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)


def outro(parts):
    print(f"\rOutro", end="")

    drum_kit = parts["drum_kit"]["part"]
    bass = parts["bass"]["part"]
    scratch = parts["scratch"]["part"]

    print(f" 1", end="")
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(ride(), 2 / 4, 1 / 4, blocking=False)
    bass.play_note(60, 2 / 4, 1 / 4)
    drum_kit.play_note(kick(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(ride(), 2 / 4, 1 / 4, blocking=False)
    bass.play_note(48, 2 / 4, 1 / 4)

    print(f" 2", end="")
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(crash(), 2 / 4, 1 / 4, blocking=False)
    bass.play_note(60, 2 / 4, 1 / 4)
    drum_kit.play_note(kick(), 2 / 4, 1 / 4, blocking=False)
    bass.play_note(48, 2 / 4, 1 / 4)

    print(f" 3", end="")
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(ride(), 2 / 4, 1 / 4, blocking=False)
    bass.play_note(60, 2 / 4, 1 / 4)
    drum_kit.play_note(kick(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    bass.play_note(48, 2 / 4, 1 / 4)

    print(f" 4", end="")
    drum_kit.play_note(kick(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(crash(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(crash(), 2 / 4, 1 / 4, blocking=False)
    bass.play_note(36, 2 / 4, 1 / 2)


def play_beat(parts):
    intro(parts)
    for _ in range(REPS):
        for _ in range(SECTION_A_REPS):
            section_a(parts)
        for _ in range(SECTION_B_REPS):
            section_b(parts)
    for _ in range(SECTION_A_REPS // 2):
        section_a(parts)
    outro(parts)


def play_melody(parts):
    print(f"\rMelody", end="")

    lead_synth = parts["lead_synth"]["part"]

    tonic = 55
    starting_tonic = tonic
    scale = Scale(tonic)
    intervals = [-1, -2, -3]
    lengths = [0.25, 0.5]

    octaves = [-2, -1, 2, 3]

    while True:
        tonic += randint(-3, 4)
        pitches = sorted(choices([scale[i] for i in range(0, 24)], k=16))
        approximate_melody_length = len(pitches) * len(intervals) * 1.5 * sum(lengths) / len(lengths)

        chord = [tonic + (12 * octave) for octave in octaves]
        print(f"{tonic=}, {chord=}, {pitches=}")

        for octave in octaves:
            lead_synth.play_note(tonic + (12 * octave), 0.25, approximate_melody_length, blocking=False)
            wait(0.25)

        for index, pitch in enumerate(pitches):
            lead_synth.play_note(pitch, 0.8, 1)
            if index % 2 == 1:
                for interval in intervals:
                    lead_synth.play_note(pitch + interval - 12, 0.5, lengths[index % len(lengths)] / 1.9)
                    lead_synth.play_note(pitch + interval - 12, 0.75, lengths[(index + 1) % len(lengths)] / 2.1)
            else:
                wait(0.25)
        else:
            lead_synth.play_note(pitches[0] + 12, 0.8, 4, blocking=False)
            lead_synth.play_note(pitches[0], 0.8, 2)
        wait(0.25)
        lead_synth.play_note(tonic + 12, 0.75, 4, blocking=False)
        lead_synth.play_note(tonic + 7, 0.5, 5, blocking=False)
        lead_synth.play_note(tonic + 4, 0.25, 3, blocking=False)
        lead_synth.play_note(tonic - 2, 0.25, 8, blocking=False)
        lead_synth.play_note(tonic - 1, 0.25, 7, blocking=False)
        lead_synth.play_note(tonic, 0.75, 6, blocking=False)
        wait(4)
        if tonic % 12 == starting_tonic % 12:
            pitch = pitches[0]
            while pitch > 0:
                lead_synth.play_note(pitch, 0.8, 1, blocking=False)
                pitch -= 1
                wait(0.25)
            break


def main():
    parts = {
        "drum_kit": {
            "name": f"Kit {choice(DRUM_KITS_I_LIKE)}",
            "soundfont": "Emu_Planet_Phatt_Hip_Hop.sf2",
        },
        "scratch": {
            "name": f"Scratch {choice(SCRATCH_KITS_I_LIKE)}",
            "soundfont": "Emu_Planet_Phatt_Hip_Hop.sf2",
        },
        "bass": {
            "name": f"Fat SynBass",
            "soundfont": "Emu_Planet_Phatt_Hip_Hop.sf2",
        },
        "lead_synth": {
            "name": f"hypersawwave",
            "soundfont": "Synths.sf2",
        },
    }

    s = setup(parts)

    fork(play_beat, [parts])
    fork(play_melody, [parts])
    s.wait_for_children_to_finish()


if __name__ == '__main__':
    main()
