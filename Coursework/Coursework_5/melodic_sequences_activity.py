import random

import math
from scamp import Session, playback_settings, wait

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

maj_offsets = {
    0: 0,
    1: 2,
    2: 4,
    3: 5,
    4: 7,
    5: 9,
    6: 11,
}


class Scale:
    def __init__(self, tonic):
        self._tonic = tonic

    def __getitem__(self, item):
        return self.note(item)

    def note(self, interval):
        interval -= 1
        note = self._tonic + maj_offsets[interval % 7] + 12 * (interval // 7)
        # print(note)
        return note


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
                self.play4(temp_instrument)
                # temp_instrument.play_note(60, 1, 1)

    def play_sin(self):
        for note in range(1000):
            pitch = math.sin(note) * 12 + 60
            print(pitch)
            self._lead_synth.play_note(pitch, 0.5, 0.5)

    def play1(self):
        start_pitch = 36
        scale = Scale(start_pitch)

        for _ in range(2):
            print("phrase one")
            self._lead_synth.play_note(scale[6], 0.5, 1)
            self._lead_synth.play_note(scale[7], 0.5, 0.5)
            self._lead_synth.play_note(scale[8], 0.5, 0.5)
            self._lead_synth.play_note(scale[7], 0.5, 0.5)
            self._lead_synth.play_note(scale[6], 0.5, 0.5)
            self._lead_synth.play_note(scale[5], 0.5, 1)

            print("phrase two")
            self._lead_synth.play_note(scale[4], 0.5, 1)
            self._lead_synth.play_note(scale[5], 0.5, 0.5)
            self._lead_synth.play_note(scale[6], 0.5, 0.5)
            self._lead_synth.play_note(scale[5], 0.5, 0.5)
            self._lead_synth.play_note(scale[4], 0.5, 0.5)
            self._lead_synth.play_note(scale[5], 0.5, 1)

    def play2(self):
        def play_trigonometry(tonic):
            scale = Scale(tonic)
            for i in range(1, 20):
                pitch = scale[random.randint(12, 36)]
                volume = (math.cos(i / 10) + 1.01) * 0.1
                length = (math.sin(i / 5) + 1.01) * 3
                print(f"{i=}: {pitch=}, {volume=}, {length=}")
                self._lead_synth.play_note(pitch, volume, length)

        tonic = 10
        for _ in range(5):
            play_trigonometry(tonic)
            tonic += 7
            play_trigonometry(tonic)
            tonic -= 2

    def play3(self):
        start = 40
        stop = 90
        step = 3
        for pitch in range(start, stop, step):
            volume = (pitch - start + 10) / (stop - start)
            length = 1
            self._lead_synth.play_note(pitch, volume, length)
            if pitch % 2 == 0:
                self._lead_synth.play_note(pitch - 1, volume, length / 4)
                self._lead_synth.play_note(pitch, volume, length / 4)
                self._lead_synth.play_note(pitch + 3, volume, length / 4)
                self._lead_synth.play_note(pitch + 4, volume, length / 4)
            else:
                self._lead_synth.play_note(pitch - 3, volume, length / 2)
                self._lead_synth.play_note(pitch - 5, volume, length / 2)
        else:
            self._lead_synth.play_note(stop + step, 1, 4)

    def play4(self, instrument=None):
        if not instrument:
            instrument = self._lead_synth
        self._session.tempo = 70
        tonic = 55
        scale = Scale(tonic)
        intervals = [-1, -2, -3]
        lengths = [0.25, 0.5]

        octaves = [-2, -1, 2, 3]

        while True:
            tonic += random.randint(-3, 4)
            self._session.tempo += random.randint(-5, 5)
            pitches = sorted(random.choices([scale[i] for i in range(0, 24)], k=12))
            approximate_melody_length = len(pitches) * len(intervals) * 1.5 * sum(lengths) / len(lengths)

            chord = [tonic + (12 * octave) for octave in octaves]
            print(f"tempo={self._session.tempo}, {tonic=}, {chord=}, {pitches=}")

            for octave in octaves:
                instrument.play_note(tonic + (12 * octave), 0.25, approximate_melody_length, blocking=False)
                wait(0.25)

            for index, pitch in enumerate(pitches):
                instrument.play_note(pitch, 1, 1)
                if index % 2 == 1:
                    for interval in intervals:
                        instrument.play_note(pitch + interval - 12, 0.5, lengths[index % len(lengths)] / 1.9)
                        instrument.play_note(pitch + interval - 12, 0.75, lengths[(index + 1) % len(lengths)] / 2.1)
                else:
                    wait(0.25)
            instrument.play_note(tonic + 12, 0.75, 4, blocking=False)
            instrument.play_note(tonic + 7, 0.5, 5, blocking=False)
            instrument.play_note(tonic + 4, 0.25, 3, blocking=False)
            instrument.play_note(tonic - 2, 0.25, 8, blocking=False)
            instrument.play_note(tonic - 1, 0.25, 7, blocking=False)
            instrument.play_note(tonic, 0.75, 6, blocking=False)
            if tonic == 69:
                break
            wait(4)
            # random.shuffle(pitches)
            # random.shuffle(octaves)
            # random.shuffle(intervals)
            # random.shuffle(lengths)


def main():
    melody = Melody(instrument="hypersawwave", tempo=80)
    # melody = Melody(instrument="SCP-Beeper", tempo=80)
    # melody = Melody(instrument="AnalogSaw1", tempo=80)
    # melody = Melody(instrument="DY-Synthe", tempo=80)
    # melody.print_sounds()
    # melody.hear_all_presets()
    # melody.play1()
    # melody.play2()
    # melody.play3()
    melody.play4()


if __name__ == '__main__':
    main()
