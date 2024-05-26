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


def print_count(beats=None, denominator=None):
    if not denominator:
        denominator = 2
    for beat in range(beats, 0, -1):
        print(f" {beat} ", end="")
        wait(1 / denominator)
    print(" ", end="")


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


def false_start_bass(parts):
    bass = parts["bass"]["part"]
    bass.play_note(kick(), 1, 2)

    wait(1)

    bass.play_note(kick(), 1, 2)


def false_start_drums(parts):
    drum_kit = parts["drum_kit"]["part"]
    drum_kit.play_note(kick(), 1, 2)

    wait(1)

    drum_kit.play_note(kick(), 1, 2)


def false_start_scratch(parts):
    scratch = parts["scratch"]["part"]
    scratch.play_note(48, 1 / 8, 2)

    wait(1)

    scratch.play_note(48, 1 / 8, 2)


def intro_bass(parts):
    bass = parts["bass"]["part"]

    # beat 1
    bass.play_note(kick(), 1, 1)

    # beat 2
    wait(1)

    # beat 3
    bass.play_note(kick(), 1, 1)

    # beat 4
    bass.play_note(kick(), 1, 1 / 8, blocking=False)
    bass.play_note(crash(), 1, 1 / 8, blocking=False)
    wait(1 / 4)
    bass.play_note(kick(), 1, 1 / 8, blocking=False)
    bass.play_note(crash(), 1, 1 / 8, blocking=False)
    wait(1 / 4)
    bass.play_note(kick(), 1, 1 / 8, blocking=False)
    bass.play_note(crash(), 1, 1 / 8, blocking=False)
    wait(1 / 4)
    bass.play_note(kick(), 1, 1 / 8, blocking=False)
    bass.play_note(crash(), 1, 1 / 8, blocking=False)
    wait(1 / 4)


def intro_drums(parts):
    drum_kit = parts["drum_kit"]["part"]

    # beat 1
    drum_kit.play_note(kick(), 1, 1)

    # beat 2
    wait(1)

    # beat 3
    drum_kit.play_note(kick(), 1, 1)

    # beat 4
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    wait(1 / 4)
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    wait(1 / 4)
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    wait(1 / 4)
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    wait(1 / 4)


def intro_scratch(parts):
    scratch = parts["scratch"]["part"]

    # beat 1
    scratch.play_note(60, 1 / 8, 1 / 4)
    scratch.play_note(62, 2 / 8, 1 / 4)
    scratch.play_note(64, 3 / 8, 1 / 4)
    scratch.play_note(65, 4 / 8, 1 / 4)

    # beat 2
    scratch.play_note(67, 5 / 8, 1 / 4)
    scratch.play_note(69, 6 / 8, 1 / 4)
    scratch.play_note(71, 7 / 8, 1 / 4)
    scratch.play_note(72, 8 / 8, 1 / 4)

    # beat 3
    scratch.play_note(72, 1 / 8, 1 / 4)
    scratch.play_note(74, 2 / 8, 1 / 4)
    scratch.play_note(76, 3 / 8, 1 / 4)
    scratch.play_note(77, 4 / 8, 1 / 4)

    # beat 4
    scratch.play_note(79, 5 / 8, 1 / 4)
    scratch.play_note(81, 6 / 8, 1 / 4)
    scratch.play_note(83, 7 / 8, 1 / 4)
    scratch.play_note(84, 8 / 8, 1 / 4)


def section_a_bass(parts):
    bass = parts["bass"]["part"]

    # beat 1
    bass.play_note(48, 1 / 8, 1, blocking=False)
    wait(1 / 2)

    # beat 2
    wait(1 / 2)

    # beat 3
    wait(1 / 4)
    bass.play_note(48, 1 / 8, uniform(1 / 8, 3 / 8), blocking=False)
    wait(1 / 4)

    # beat 4
    wait(1 / 4)

    bass.play_note(46, 1 / 8, 1 / 4, blocking=False)
    wait(1 / 4)


def section_a_drums(parts):
    drum_kit = parts["drum_kit"]["part"]

    # beat 1
    drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(kick(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)
    drum_kit.play_note(hat(), 3 / 4, 1 / 4)

    # beat 2
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(kick(), 1 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)
    drum_kit.play_note(hat(), 3 / 4, 1 / 4)

    # beat 3
    drum_kit.play_note(kick(), 2 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)
    if choice([True, False]):
        drum_kit.play_note(snare(), 3 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(hat(), 3 / 4, 1 / 4)

    # beat 4
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(kick(), 1 / 4, 1 / 4, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(72, 1 / 8, 1 / 4, blocking=False)
    drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)

    if choice([True, False]):
        drum_kit.play_note(snare(), 3 / 4, 1 / 4, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(kick(), 3 / 4, 1 / 2, blocking=False)
    if choice([True, False]):
        drum_kit.play_note(crash(), 1, 1 / 2, blocking=False)
    drum_kit.play_note(hat(), 3 / 4, 1 / 4)


def section_a_scratch(parts):
    scratch = parts["scratch"]["part"]

    # beat 1
    wait(1 / 2)

    # beat 2
    wait(1 / 2)

    # beat 3
    wait(1 / 2)

    # beat 4
    wait(1 / 4)

    if choice([True, False]):
        scratch.play_note(84, 1 / 8, 3 / 4, blocking=False)
    wait(1 / 4)


def section_b_bass(parts):
    bass = parts["bass"]["part"]

    # beat 1
    bass.play_note(60, 1 / 8, uniform(3 / 4, 1), blocking=False)
    wait(1)

    # beat 2
    wait(1 / 2)

    bass.play_note(59, 1 / 8, uniform(1 / 4, 3 / 4), blocking=False)
    wait(1 / 2)

    # beat 3
    wait(1 / 2)

    bass.play_note(58, 1 / 8, uniform(3 / 8, 5 / 8), blocking=False)
    wait(1 / 2)

    # beat 4
    bass.play_note(57, 1 / 8, uniform(3 / 8, 5 / 8), blocking=False)
    wait(1 / 2)

    bass.play_note(56, 1 / 8, 1 / 2, blocking=False)
    wait(1 / 2)


def section_b_drums(parts):
    drum_kit = parts["drum_kit"]["part"]

    # beat 1
    drum_kit.play_note(kick(), 2 / 4, 1, blocking=False)
    drum_kit.play_note(OPEN_HAT, 3 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)

    # beat 2
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    drum_kit.play_note(kick(), 2 / 4, 1, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    # beat 3
    drum_kit.play_note(hat(), 3 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)

    # beat 4
    drum_kit.play_note(kick(), 2 / 4, 1, blocking=False)
    drum_kit.play_note(crash(), random(), 1 / 4)
    drum_kit.play_note(ride(), random(), 1 / 4)

    drum_kit.play_note(ride(), random(), 1 / 4)
    drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
    drum_kit.play_note(ride(), random(), 1 / 4)


def section_b_scratch(parts):
    scratch = parts["scratch"]["part"]

    # beat 1
    scratch.play_note(72, 8 / 8, 1 / 4, blocking=False)
    wait(1)

    # beat 2
    scratch.play_note(72, 8 / 8, 1 / 2, blocking=False)
    wait(1 / 2)

    scratch.play_note(75, 8 / 8, 1 / 4, blocking=False)
    wait(1 / 2)

    # beat 3
    wait(1 / 2)

    scratch.play_note(72, 8 / 8, 1 / 2, blocking=False)
    wait(1 / 2)

    # beat 4
    wait(1 / 2)

    wait(1 / 4)
    scratch.play_note(78, 8 / 8, 1 / 2, blocking=False)
    wait(1 / 4)


def outro_bass(parts):
    bass = parts["bass"]["part"]

    # beat 1
    bass.play_note(60, 2 / 4, 1 / 4)
    bass.play_note(48, 2 / 4, 1 / 4)

    # beat 2
    bass.play_note(60, 2 / 4, 1 / 4)
    bass.play_note(48, 2 / 4, 1 / 4)

    # beat 3
    bass.play_note(60, 2 / 4, 1 / 6)
    bass.play_note(53, 2 / 4, 1 / 6)
    bass.play_note(48, 2 / 4, 1 / 6)

    # beat 4
    bass.play_note(36, 2 / 4, 1 / 2)


def outro_drums(parts):
    drum_kit = parts["drum_kit"]["part"]

    # beat 1
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(ride(), 2 / 4, 1 / 4, blocking=False)
    wait(1 / 4)
    drum_kit.play_note(kick(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(ride(), 2 / 4, 1 / 4, blocking=False)
    wait(1 / 4)

    # beat 2
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(crash(), 2 / 4, 1 / 4, blocking=False)
    wait(1 / 4)
    drum_kit.play_note(kick(), 2 / 4, 1 / 4, blocking=False)
    wait(1 / 4)

    # beat 3
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(ride(), 2 / 4, 1 / 4, blocking=False)
    wait(1 / 4)
    drum_kit.play_note(kick(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    wait(1 / 4)

    # beat 4
    drum_kit.play_note(kick(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(snare(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(crash(), 2 / 4, 1 / 4, blocking=False)
    drum_kit.play_note(crash(), 2 / 4, 1 / 4, blocking=False)
    wait(1 / 2)


def outro_scratch(parts):
    scratch = parts["scratch"]["part"]

    # beat 1
    wait(1 / 2)

    # beat 2
    wait(1 / 2)

    # beat 3
    wait(1 / 2)

    # beat 4
    wait(1 / 2)


def play_melody(parts):
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


def false_start(s: Session, parts):
    print(f"\rStarting", end="")
    fork(print_count, [5, 1])
    fork(false_start_bass, [parts])
    fork(false_start_drums, [parts])
    fork(false_start_scratch, [parts])
    s.wait_for_children_to_finish()


def intro(s: Session, parts):
    print(f"\rIntro", end="")
    fork(print_count, [8, 2])
    fork(intro_bass, [parts])
    fork(intro_drums, [parts])
    fork(intro_scratch, [parts])
    s.wait_for_children_to_finish()


def section_a(s: Session, parts):
    print(f"\rSection A", end="")
    fork(print_count, [4, 2])
    fork(section_a_drums, [parts])
    fork(section_a_bass, [parts])
    fork(section_a_scratch, [parts])
    s.wait_for_children_to_finish()


def section_b(s: Session, parts):
    print(f"\rSection B", end="")
    fork(print_count, [8, 2])
    fork(section_b_drums, [parts])
    fork(section_b_bass, [parts])
    fork(section_b_scratch, [parts])
    s.wait_for_children_to_finish()


def outro(s: Session, parts):
    print(f"\rOutro", end="")
    fork(print_count, [7, 4])
    fork(outro_bass, [parts])
    fork(outro_drums, [parts])
    fork(outro_scratch, [parts])
    s.wait_for_children_to_finish()


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

    intro(s, parts)

    for rep in range(REPS):
        for _ in range(SECTION_A_REPS - 2 * rep):
            section_a(s, parts)
        for _ in range(SECTION_B_REPS - 2 * rep):
            section_b(s, parts)
    for _ in range(SECTION_A_REPS // 2):
        section_a(s, parts)

    outro(s, parts)


if __name__ == '__main__':
    main()
