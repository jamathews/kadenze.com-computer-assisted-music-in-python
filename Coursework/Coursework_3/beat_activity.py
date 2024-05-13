from datetime import datetime
from random import choice
from random import uniform

from scamp import *

playback_settings.recording_file_path = f"{datetime.now().isoformat()}.wav"

MAX_TEMPO = 90
MIN_TEMPO = 60

ACOUSTIC_SNARE = 38
ELECTRIC_SNARE = 40
HAND_CLAP = 39

KICK = 35

CLOSED_HAT = 42
OPEN_HAT = 46
PEDAL_HAT = 44

DRUM_KITS_I_LIKE = [2, 3, 5, 8, 9]
SCRATCH_KITS_I_LIKE = [1, 2, 7, 9, 10, 13, 17]


def get_session() -> Session:
    s = Session(default_soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
    s.tempo = uniform(MIN_TEMPO, MAX_TEMPO)
    return s


def hat() -> int:
    return choice([CLOSED_HAT, OPEN_HAT, PEDAL_HAT])


def snare() -> int:
    return choice([ACOUSTIC_SNARE, ELECTRIC_SNARE, HAND_CLAP])


def main():
    def intro():
        drum_kit.play_note(KICK, 1, 1 / 2, blocking=False)
        scratch.play_note(48, 1 / 8, 2)

        drum_kit.play_note(KICK, 1, 1 / 2, blocking=False)
        scratch.play_note(48, 1 / 8, 2)

        drum_kit.play_note(KICK, 1, 1 / 2, blocking=False)
        scratch.play_note(60, 1 / 8, 1 / 4)
        scratch.play_note(62, 2 / 8, 1 / 4)
        scratch.play_note(64, 3 / 8, 1 / 4)
        scratch.play_note(65, 4 / 8, 1 / 4)

        scratch.play_note(67, 5 / 8, 1 / 4)
        scratch.play_note(69, 6 / 8, 1 / 4)
        scratch.play_note(71, 7 / 8, 1 / 4)
        scratch.play_note(72, 8 / 8, 1 / 4)

        drum_kit.play_note(KICK, 1, 1 / 2, blocking=False)
        scratch.play_note(72, 1 / 8, 1 / 4)
        scratch.play_note(74, 2 / 8, 1 / 4)
        scratch.play_note(76, 3 / 8, 1 / 4)
        scratch.play_note(77, 4 / 8, 1 / 4)

        drum_kit.play_note(KICK, 1, 1 / 2, blocking=False)
        scratch.play_note(79, 5 / 8, 1 / 4)
        drum_kit.play_note(KICK, 1, 1 / 2, blocking=False)
        scratch.play_note(81, 6 / 8, 1 / 4)
        drum_kit.play_note(KICK, 1, 1 / 2, blocking=False)
        scratch.play_note(83, 7 / 8, 1 / 4)
        drum_kit.play_note(KICK, 1, 1 / 2, blocking=False)
        scratch.play_note(84, 8 / 8, 1 / 4)

    def body():
        drum_kit.play_note(KICK, 1, 1 / 2, blocking=False)
        drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)
        drum_kit.play_note(hat(), 3 / 4, 1 / 4)

        drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
        if choice([True, False]):
            drum_kit.play_note(KICK, 1 / 4, 1 / 2, blocking=False)
        drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)
        drum_kit.play_note(hat(), 3 / 4, 1 / 4)

        drum_kit.play_note(KICK, 2 / 4, 1 / 2, blocking=False)
        drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)
        if choice([True, False]):
            drum_kit.play_note(snare(), 3 / 4, 1 / 4, blocking=False)
        drum_kit.play_note(hat(), 3 / 4, 1 / 4)

        drum_kit.play_note(ACOUSTIC_SNARE, 3 / 4, 1 / 2, blocking=False)
        if choice([True, False]):
            drum_kit.play_note(KICK, 1 / 4, 1 / 4, blocking=False)
        if choice([True, False]):
            scratch.play_note(72, 1 / 8, 1 / 4, blocking=False)
        drum_kit.play_note(CLOSED_HAT, 1 / 8, 1 / 4)

        if choice([True, False]):
            drum_kit.play_note(snare(), 3 / 4, 1 / 4, blocking=False)
        if choice([True, False]):
            drum_kit.play_note(KICK, 3 / 4, 1 / 2, blocking=False)
        if choice([True, False]):
            scratch.play_note(84, 1 / 8, 3 / 4, blocking=False)
        drum_kit.play_note(hat(), 3 / 4, 1 / 4)

    main_session = get_session()
    # print_session_info(main_session)

    drum_kit = main_session.new_part(f"Kit {choice(DRUM_KITS_I_LIKE)}")
    scratch = main_session.new_part(f"Scratch {choice(SCRATCH_KITS_I_LIKE)}")

    intro()
    while True:
        body()


def print_session_info(current_session):
    current_session.print_family_tree()
    current_session.print_available_midi_output_devices()
    current_session.print_available_midi_input_devices()
    current_session.print_default_soundfont_presets()
    print(current_session.tempo)


if __name__ == '__main__':
    main()
