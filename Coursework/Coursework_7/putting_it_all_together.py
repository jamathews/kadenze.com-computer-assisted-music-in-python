from datetime import datetime
from random import choice
from random import randint
from random import random
from random import uniform

from scamp import *

from scale import Scale

TONIC = 48

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


def setup(config):
    new_parts = config["parts"]
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
    scratch.play_note(TONIC, 1 / 8, 2)

    wait(1)

    scratch.play_note(TONIC, 1 / 8, 2)


def intro_bass(config):
    bass = config["parts"]["bass"]["part"]

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


def intro_drums(config):
    drum_kit = config["parts"]["drum_kit"]["part"]

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


def intro_scratch(config):
    scratch = config["parts"]["scratch"]["part"]

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


def section_a_melody(config):
    lead_synth = config["parts"]["lead_synth"]["part"]
    scale = config["scale"]

    # beat 1 & 2
    lead_synth.play_note(scale[randint(8, 16)], 1, 1 / 3)
    lead_synth.play_note(scale[randint(8, 24)], 7 / 8, 1 / 3)
    lead_synth.play_note(scale[randint(1, 16)], 3 / 4, 1 / 3)

    # beat 3
    wait(1 / 4)
    wait(1 / 4)

    # beat 4
    wait(1 / 4)
    if choice([True, False]):
        lead_synth.play_note(scale[randint(1, 16)], 8 / 10, 1 / 12)
        lead_synth.play_note(scale[randint(1, 16)], 9 / 10, 1 / 12)
        lead_synth.play_note(scale[randint(1, 16)], 1, 1 / 12)
    else:
        wait(1 / 4)


def section_a_bass(config):
    bass = config["parts"]["bass"]["part"]
    scale = config["scale"]

    # beat 1
    bass.play_note(scale[1], 1 / 8, 1, blocking=False)
    wait(1 / 2)

    # beat 2
    wait(1 / 2)

    # beat 3
    wait(1 / 4)
    bass.play_note(scale[1], 1 / 8, uniform(1 / 8, 3 / 8), blocking=False)
    wait(1 / 4)

    # beat 4
    wait(1 / 4)

    bass.play_note(scale[-2] - 1, 1 / 8, 1 / 4, blocking=False)
    wait(1 / 4)


def section_a_drums(config):
    drum_kit = config["parts"]["drum_kit"]["part"]

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


def section_a_scratch(config):
    scratch = config["parts"]["scratch"]["part"]

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


def section_b_melody(config):
    lead_synth = config["parts"]["lead_synth"]["part"]
    scale = config["scale"]

    # beat 1
    for _ in range(4):
        lead_synth.play_note(scale[choice([23, 24])], uniform(0.5, 1), 1 / 16)
        wait(1 / 16)

    # beat 2
    if choice([True, False]):
        for _ in range(4):
            lead_synth.play_note(scale[randint(12, 16)], uniform(0.5, 1), 1 / 8)
            wait(1 / 8)
    else:
        wait(1)

    # beat 3 & 4
    durations = []
    while sum(durations) < 2:
        durations.append(randint(1, 7) / 8)
    else:
        if sum(durations) > 2:
            durations[-1] = 2 - sum(durations[:-1])
    for duration in durations:
        lead_synth.play_note(scale[randint(24, 28)], uniform(0.5, 1), duration)


def section_b_bass(config):
    bass = config["parts"]["bass"]["part"]
    scale = config["scale"]

    # beat 1
    bass.play_note(scale[8], 1 / 8, uniform(3 / 4, 1), blocking=False)
    wait(1)

    # beat 2
    wait(1 / 2)

    bass.play_note(scale[7], 1 / 8, uniform(1 / 4, 3 / 4), blocking=False)
    wait(1 / 2)

    # beat 3
    wait(1 / 2)

    bass.play_note(scale[7] - 1, 1 / 8, uniform(3 / 8, 5 / 8), blocking=False)
    wait(1 / 2)

    # beat 4
    bass.play_note(scale[6], 1 / 8, uniform(3 / 8, 5 / 8), blocking=False)
    wait(1 / 2)

    bass.play_note(scale[6] - 1, 1 / 8, 1 / 2, blocking=False)
    wait(1 / 2)


def section_b_drums(config):
    drum_kit = config["parts"]["drum_kit"]["part"]

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


def section_b_scratch(config):
    scratch = config["parts"]["scratch"]["part"]

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


def outro_bass(config):
    bass = config["parts"]["bass"]["part"]
    scale = config["scale"]

    # beat 1
    bass.play_note(scale[8], 2 / 4, 1 / 4)
    bass.play_note(scale[1], 2 / 4, 1 / 4)

    # beat 2
    bass.play_note(scale[8], 2 / 4, 1 / 4)
    bass.play_note(scale[1], 2 / 4, 1 / 4)

    # beat 3
    bass.play_note(scale[8], 2 / 4, 1 / 6)
    bass.play_note(scale[4], 2 / 4, 1 / 6)
    bass.play_note(scale[1], 2 / 4, 1 / 6)

    # beat 4
    bass.play_note(scale[-8], 2 / 4, 1 / 2)


def outro_drums(config):
    drum_kit = config["parts"]["drum_kit"]["part"]

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


def outro_scratch(config):
    scratch = config["parts"]["scratch"]["part"]

    # beat 1
    wait(1 / 2)

    # beat 2
    wait(1 / 2)

    # beat 3
    wait(1 / 2)

    # beat 4
    wait(1 / 2)


def false_start(s: Session, parts):
    print(f"\rStarting", end="")
    fork(print_count, [5, 1])
    fork(false_start_bass, [parts])
    fork(false_start_drums, [parts])
    fork(false_start_scratch, [parts])
    s.wait_for_children_to_finish()


def intro(s: Session, config):
    print(f"\rIntro", end="")
    fork(print_count, [8, 2])
    fork(intro_bass, [config])
    fork(intro_drums, [config])
    fork(intro_scratch, [config])
    s.wait_for_children_to_finish()


def section_a(s: Session, config):
    print(f"\rSection A", end="")
    fork(print_count, [4, 2])
    fork(section_a_drums, [config])
    fork(section_a_melody, [config])
    fork(section_a_bass, [config])
    fork(section_a_scratch, [config])
    s.wait_for_children_to_finish()


def section_b(s: Session, config):
    print(f"\rSection B", end="")
    fork(print_count, [8, 2])
    fork(section_b_drums, [config])
    fork(section_b_melody, [config])
    fork(section_b_bass, [config])
    fork(section_b_scratch, [config])
    s.wait_for_children_to_finish()


def outro(s: Session, config):
    print(f"\rOutro", end="")
    fork(print_count, [7, 4])
    fork(outro_bass, [config])
    fork(outro_drums, [config])
    fork(outro_scratch, [config])
    s.wait_for_children_to_finish()


def main():
    config = {
        "parts": {
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
        },
        "scale": Scale(TONIC)
    }

    s = setup(config)

    intro(s, config)

    for rep in range(REPS):
        for _ in range(SECTION_A_REPS - 2 * rep):
            section_a(s, config)
        for _ in range(SECTION_B_REPS - 2 * rep):
            section_b(s, config)
    for _ in range(SECTION_A_REPS // 2):
        section_a(s, config)

    outro(s, config)


if __name__ == '__main__':
    main()
