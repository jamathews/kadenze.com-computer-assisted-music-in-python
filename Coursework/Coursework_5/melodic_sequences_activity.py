import math
from scamp import Session, playback_settings


# PRESETS FOR Synths.sf2
#    Preset[000:000] LD-AcidSQneutral 2 bag(s) from #0
#    Preset[000:001] LD-DanceTrance 2 bag(s) from #2
#    Preset[000:002] CandyBee 2 bag(s) from #4
#    Preset[000:003] SCP-Beeper 2 bag(s) from #6
#    Preset[000:004] AnalogSaw1 2 bag(s) from #8
#    Preset[000:005] PlasticStrings 2 bag(s) from #10
#    Preset[000:006] BS-DirtySub 2 bag(s) from #12
#    Preset[000:007] hypersawwave 2 bag(s) from #14
#    Preset[000:008] PD-Sinewave 2 bag(s) from #16
#    Preset[000:009] LD-PolySpecialMono 2 bag(s) from #18
#    Preset[000:010] PulseWobblerA 2 bag(s) from #20
#    Preset[000:011] SuperSawA 2 bag(s) from #22
#    Preset[000:012] DY-Synthe 2 bag(s) from #24
#    Preset[000:013] SupSawA 2 bag(s) from #26


def maj(tonic):
    return {
        1: tonic + 0,
        2: tonic + 2,
        3: tonic + 4,
        4: tonic + 5,
        5: tonic + 7,
        6: tonic + 9,
        7: tonic + 11,
        8: tonic + 12,
        9: tonic + 14,
        10: tonic + 16,
        11: tonic + 17,
        12: tonic + 19,
        13: tonic + 21,
        14: tonic + 23,
        15: tonic + 24,
    }


class Melody:
    def __init__(self, soundfont="Synths.sf2", wav=None, tempo=90, instrument="LD-AcidSQneutral"):
        if wav:
            playback_settings.recording_file_path = wav

        self._session = Session(default_soundfont=soundfont)
        self._session.tempo = tempo
        self._lead_synth = self._session.new_part(instrument)

    def print_sounds(self):
        self._session.print_default_soundfont_presets()

    def hear_all_presets(self):
        for bank in range(1):
            for preset in range(14):
                temp_instrument = self._session.new_part(preset=(bank, preset))
                if not temp_instrument:
                    return
                print(f"{bank=}: {preset=}")
                temp_instrument.play_note(60, 1, 1)

    def play_sin(self):
        for note in range(1000):
            pitch = math.sin(note) * 12 + 60
            print(pitch)
            self._lead_synth.play_note(pitch, 0.5, 0.5)

    def play(self):
        start_pitch = 36
        scale = maj(start_pitch)
        for _ in range(2):
            self._lead_synth.play_note(scale[6], 0.5, 1)
            self._lead_synth.play_note(scale[7], 0.5, 0.5)
            self._lead_synth.play_note(scale[8], 0.5, 0.5)
            self._lead_synth.play_note(scale[7], 0.5, 0.5)
            self._lead_synth.play_note(scale[6], 0.5, 0.5)
            self._lead_synth.play_note(scale[5], 0.5, 1)

            self._lead_synth.play_note(scale[4], 0.5, 1)
            self._lead_synth.play_note(scale[5], 0.5, 0.5)
            self._lead_synth.play_note(scale[6], 0.5, 0.5)
            self._lead_synth.play_note(scale[5], 0.5, 0.5)
            self._lead_synth.play_note(scale[4], 0.5, 0.5)
            self._lead_synth.play_note(scale[5], 0.5, 1)


def main():
    melody = Melody(instrument="CandyBee", tempo=70)
    # melody.print_sounds()
    # melody.hear_all_presets()
    melody.play()


if __name__ == '__main__':
    main()