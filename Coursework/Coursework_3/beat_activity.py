import random
from datetime import datetime
from random import choice
from random import uniform

from scamp import *

REPS = 2
SECTION_A_REPS = 8
SECTION_B_REPS = 4

SOUNDFONT = "Emu_Planet_Phatt_Hip_Hop.sf2"
#
# PRESETS FOR Emu_Planet_Phatt_Hip_Hop.sf2
#    Preset[001:116] E-mu Systems  1997 1 bag(s) from #0
#    Preset[128:009] Kit 10 1 bag(s) from #1
#    Preset[128:008] Kit 9 1 bag(s) from #2
#    Preset[128:007] Kit 8 1 bag(s) from #3
#    Preset[128:006] Kit 7 1 bag(s) from #4
#    Preset[128:005] Kit 6 1 bag(s) from #5
#    Preset[128:004] Kit 5 1 bag(s) from #6
#    Preset[128:003] Kit 4 1 bag(s) from #7
#    Preset[128:002] Kit 3 1 bag(s) from #8
#    Preset[128:001] Kit 2 1 bag(s) from #9
#    Preset[128:000] Kit 1 1 bag(s) from #10
#    Preset[000:001] SE Sub 1            1 bag(s) from #11
#    Preset[000:002] SE Sub 2            1 bag(s) from #12
#    Preset[000:003] SE Sub 3            1 bag(s) from #13
#    Preset[000:004] SE Sub 4            1 bag(s) from #14
#    Preset[000:005] SE Sub 5            1 bag(s) from #15
#    Preset[000:006] SE Sub 6            1 bag(s) from #16
#    Preset[000:007] SE Sub 7            1 bag(s) from #17
#    Preset[000:008] SE Sub 8            1 bag(s) from #18
#    Preset[000:009] SE Sub 9            1 bag(s) from #19
#    Preset[000:010] SE Sub 10           1 bag(s) from #20
#    Preset[000:011] SE Sub 11           1 bag(s) from #21
#    Preset[000:012] Subtle Bass         1 bag(s) from #22
#    Preset[000:013] Bass Slap 1         1 bag(s) from #23
#    Preset[000:014] Bass Slap 2         1 bag(s) from #24
#    Preset[000:015] FingerBass1         1 bag(s) from #25
#    Preset[000:016] FingerBass2         1 bag(s) from #26
#    Preset[000:017] EP Bass 1           1 bag(s) from #27
#    Preset[000:018] EP Bass 2a          1 bag(s) from #28
#    Preset[000:019] EP Bass 2b          1 bag(s) from #29
#    Preset[000:020] UprightBass         1 bag(s) from #30
#    Preset[000:021] Fretless 1          1 bag(s) from #31
#    Preset[000:022] Fretless 2          1 bag(s) from #32
#    Preset[000:023] Fretless 3          1 bag(s) from #33
#    Preset[000:024] Fretless 4          1 bag(s) from #34
#    Preset[000:025] Street Bass         1 bag(s) from #35
#    Preset[000:026] TBazz               1 bag(s) from #36
#    Preset[000:027] Dope Bass 1         1 bag(s) from #37
#    Preset[000:028] Dope Bass 2         1 bag(s) from #38
#    Preset[000:029] DopeBassHit         1 bag(s) from #39
#    Preset[000:030] Slider Bass         1 bag(s) from #40
#    Preset[000:031] Saw Bass            1 bag(s) from #41
#    Preset[000:032] Mini Saw            1 bag(s) from #42
#    Preset[000:033] Ultimate 2a         1 bag(s) from #43
#    Preset[000:034] Ultimate 2b         1 bag(s) from #44
#    Preset[000:035] BigSaw Bass         1 bag(s) from #45
#    Preset[000:036] Big Mini 1          1 bag(s) from #46
#    Preset[000:037] Big Mini 2          1 bag(s) from #47
#    Preset[000:038] Mini                1 bag(s) from #48
#    Preset[000:039] Filter Bass         1 bag(s) from #49
#    Preset[000:040] Fat SynBass         1 bag(s) from #50
#    Preset[000:041] Planet Bass         1 bag(s) from #51
#    Preset[000:042] Syn Tone            1 bag(s) from #52
#    Preset[000:043] BassBalls1          1 bag(s) from #53
#    Preset[000:044] BassBalls2          1 bag(s) from #54
#    Preset[000:045] Bas Boy Syn         1 bag(s) from #55
#    Preset[000:046] All Purpose         1 bag(s) from #56
#    Preset[000:047] Standard  Bass      1 bag(s) from #57
#    Preset[000:048] Buzz Bass           1 bag(s) from #58
#    Preset[000:049] Home Bass           1 bag(s) from #59
#    Preset[000:050] Gtr Mutes           1 bag(s) from #60
#    Preset[000:051] Sine Wave           1 bag(s) from #61
#    Preset[000:052] Saw Wave            1 bag(s) from #62
#    Preset[000:053] Synth Axe           1 bag(s) from #63
#    Preset[000:054] Synth Axe 2         1 bag(s) from #64
#    Preset[000:055] Zippy Lead          1 bag(s) from #65
#    Preset[000:056] Mini OD2            1 bag(s) from #66
#    Preset[000:057] Bell Synth          1 bag(s) from #67
#    Preset[000:058] BuzzSynth 1         1 bag(s) from #68
#    Preset[000:059] BuzzSynth 2         1 bag(s) from #69
#    Preset[000:060] Dance Lead          1 bag(s) from #70
#    Preset[000:061] Worm Lead 1         1 bag(s) from #71
#    Preset[000:062] Worm Lead 2         1 bag(s) from #72
#    Preset[000:063] Worm Lead 3         1 bag(s) from #73
#    Preset[000:064] Worm Lead 4         1 bag(s) from #74
#    Preset[000:065] Worm Lead 5         1 bag(s) from #75
#    Preset[000:066] Worm Lead 6         1 bag(s) from #76
#    Preset[000:067] ElectriWorm         1 bag(s) from #77
#    Preset[000:068] Electron            1 bag(s) from #78
#    Preset[000:069] Tone Organ          1 bag(s) from #79
#    Preset[000:070] Disco Organ         1 bag(s) from #80
#    Preset[000:071] DX Organ            1 bag(s) from #81
#    Preset[000:072] JX Organ            1 bag(s) from #82
#    Preset[000:073] Oddd Organ          1 bag(s) from #83
#    Preset[000:074] Clavinet            1 bag(s) from #84
#    Preset[000:075] Classic EP          1 bag(s) from #85
#    Preset[000:076] FM EP 1a            1 bag(s) from #86
#    Preset[000:077] FM EP 1b            1 bag(s) from #87
#    Preset[000:078] Tine EP             1 bag(s) from #88
#    Preset[000:079] Pretty EP           1 bag(s) from #89
#    Preset[000:080] EP Fog              1 bag(s) from #90
#    Preset[000:081] EP Roll1 C          1 bag(s) from #91
#    Preset[000:082] EP Roll2 F6         1 bag(s) from #92
#    Preset[000:083] EP Roll3Bbm         1 bag(s) from #93
#    Preset[000:084] Mute Tpt            1 bag(s) from #94
#    Preset[000:085] Tpt FX 1            1 bag(s) from #95
#    Preset[000:086] Tpt FX 2            1 bag(s) from #96
#    Preset[000:087] Bari Wave           1 bag(s) from #97
#    Preset[000:088] P5 Brass            1 bag(s) from #98
#    Preset[000:089] Spacy Tpt           1 bag(s) from #99
#    Preset[000:090] Sax Riff Eb         1 bag(s) from #100
#    Preset[000:091] Wack Tpt 1 bag(s) from #101
#    Preset[000:092] Synth Flute         1 bag(s) from #102
#    Preset[000:093] Boink               1 bag(s) from #103
#    Preset[000:094] Brasss Bb           1 bag(s) from #104
#    Preset[000:095] Harmonica           1 bag(s) from #105
#    Preset[000:096] Gtr Wah Bm          1 bag(s) from #106
#    Preset[000:097] Alt Gtr Wah         1 bag(s) from #107
#    Preset[000:098] DisTar Pad          1 bag(s) from #108
#    Preset[000:099] SynthHiStrg         1 bag(s) from #109
#    Preset[000:100] SynthEnsble         1 bag(s) from #110
#    Preset[000:101] Synth Vox           1 bag(s) from #111
#    Preset[000:102] Soft Syn            1 bag(s) from #112
#    Preset[000:103] MoodStrings         1 bag(s) from #113
#    Preset[000:104] Xylo Pad            1 bag(s) from #114
#    Preset[000:105] Big Planet          1 bag(s) from #115
#    Preset[000:106] Dreamyy  C          1 bag(s) from #116
#    Preset[000:107] Phat Pad            1 bag(s) from #117
#    Preset[000:108] Under Pad Fm        1 bag(s) from #118
#    Preset[000:109] Science             1 bag(s) from #119
#    Preset[000:110] MusiCrowd           1 bag(s) from #120
#    Preset[000:111] Crowd 2             1 bag(s) from #121
#    Preset[000:112] Crowd 2 NTP         1 bag(s) from #122
#    Preset[000:113] Dirt                1 bag(s) from #123
#    Preset[000:114] Dirt NTP            1 bag(s) from #124
#    Preset[000:115] Dirt 2              1 bag(s) from #125
#    Preset[000:116] Dirt 2 NTP          1 bag(s) from #126
#    Preset[000:117] Dirt 3              1 bag(s) from #127
#    Preset[000:118] Dirt 3 NTP          1 bag(s) from #128
#    Preset[000:119] Oow                 1 bag(s) from #129
#    Preset[000:120] Soul Oohs           1 bag(s) from #130
#    Preset[000:121] Dance Hits          1 bag(s) from #131
#    Preset[000:122] FX Hits             1 bag(s) from #132
#    Preset[000:123] Gtr Riffs           1 bag(s) from #133
#    Preset[000:124] Bass Hits 1         1 bag(s) from #134
#    Preset[000:125] Bass Hits 2         1 bag(s) from #135
#    Preset[000:126] Brass Hits          1 bag(s) from #136
#    Preset[000:127] Vox Hits            1 bag(s) from #137
#    Preset[001:001] Scratches 1 bag(s) from #138
#    Preset[001:002] Kicks 1 bag(s) from #139
#    Preset[001:003] Snares 1 bag(s) from #140
#    Preset[001:004] Toms 1 bag(s) from #141
#    Preset[001:005] Timbales 1 bag(s) from #142
#    Preset[001:006] CongasBngos 1 bag(s) from #143
#    Preset[001:007] Hats 1 bag(s) from #144
#    Preset[001:008] Cymbals 1 bag(s) from #145
#    Preset[001:009] Shakers 1 bag(s) from #146
#    Preset[001:010] Bells 1 bag(s) from #147
#    Preset[001:011] Blocks 1 bag(s) from #148
#    Preset[001:012] Tams 1 bag(s) from #149
#    Preset[001:013] Claps 1 bag(s) from #150
#    Preset[001:014] Snaps 1 bag(s) from #151
#    Preset[001:015] Misc Perc 1 bag(s) from #152
#    Preset[001:016] Tpt FX 1 1 bag(s) from #153
#    Preset[001:017] Tpt FX 2 1 bag(s) from #154
#    Preset[001:018] Tpt FX 3 1 bag(s) from #155
#    Preset[001:019] Tpt FX 4 1 bag(s) from #156
#    Preset[001:020] Tpt FX 5 1 bag(s) from #157
#    Preset[001:021] Sax FX 1 1 bag(s) from #158
#    Preset[001:022] Sax FX 2 1 bag(s) from #159
#    Preset[001:023] Brass Hit 1 Bbm 1 bag(s) from #160
#    Preset[001:024] Brass Hit 2 1 bag(s) from #161
#    Preset[001:025] Brass Hit 3 1 bag(s) from #162
#    Preset[001:026] Brass Hit 4 1 bag(s) from #163
#    Preset[001:027] Brass Hit 5 1 bag(s) from #164
#    Preset[001:028] Brass Hit 6 1 bag(s) from #165
#    Preset[001:029] Brass Hit 7 1 bag(s) from #166
#    Preset[001:030] Brass Hit 8 1 bag(s) from #167
#    Preset[001:031] Brass Hit 9 1 bag(s) from #168
#    Preset[001:032] Brass Hit 10 1 bag(s) from #169
#    Preset[001:033] Brass Hit 11 1 bag(s) from #170
#    Preset[001:034] Brass Hit 12 1 bag(s) from #171
#    Preset[001:035] Brass Hit 13 1 bag(s) from #172
#    Preset[001:036] Brass Hit14 1 bag(s) from #173
#    Preset[001:037] Brass Hit15 1 bag(s) from #174
#    Preset[001:038] Brass Hit16 1 bag(s) from #175
#    Preset[001:039] Brass Hit17 1 bag(s) from #176
#    Preset[001:040] Brass Hit18 1 bag(s) from #177
#    Preset[001:041] Dance Hit 1 1 bag(s) from #178
#    Preset[001:042] Dance Hit 2 1 bag(s) from #179
#    Preset[001:043] Dance Hit 3 1 bag(s) from #180
#    Preset[001:044] Dance Hit 4 1 bag(s) from #181
#    Preset[001:045] Dance Hit 5 1 bag(s) from #182
#    Preset[001:046] Dance Hit 6 1 bag(s) from #183
#    Preset[001:047] Dance Hit 7 1 bag(s) from #184
#    Preset[001:048] Dance Hit 8 1 bag(s) from #185
#    Preset[001:049] Dance Hit 9 1 bag(s) from #186
#    Preset[001:050] Dance Hit10 1 bag(s) from #187
#    Preset[001:051] FX Hit 1 1 bag(s) from #188
#    Preset[001:052] FX Hit 2 1 bag(s) from #189
#    Preset[001:053] FX Hit 3 1 bag(s) from #190
#    Preset[001:054] FX Hit 4 1 bag(s) from #191
#    Preset[001:055] FX Hit 5 1 bag(s) from #192
#    Preset[001:056] FX Hit 6 1 bag(s) from #193
#    Preset[001:057] FX Hit 7 1 bag(s) from #194
#    Preset[001:058] Gtr Hit 1 1 bag(s) from #195
#    Preset[001:059] Gtr Hit 2 1 bag(s) from #196
#    Preset[001:060] Gtr Hit 3 1 bag(s) from #197
#    Preset[001:061] Gtr Hit 4 1 bag(s) from #198
#    Preset[001:062] Gtr Hit 5 1 bag(s) from #199
#    Preset[001:063] Gtr Hit 6 1 bag(s) from #200
#    Preset[001:064] Gtr Hit 7 1 bag(s) from #201
#    Preset[001:065] Gtr Hit 8 1 bag(s) from #202
#    Preset[001:066] Gtr Hit 9 1 bag(s) from #203
#    Preset[001:067] Gtr Hit 10 1 bag(s) from #204
#    Preset[001:068] Gtr Hit 11 1 bag(s) from #205
#    Preset[001:069] Gtr Hit 12 1 bag(s) from #206
#    Preset[001:070] Gtr Hit 13 1 bag(s) from #207
#    Preset[001:071] Gtr Hit 14 1 bag(s) from #208
#    Preset[001:072] Gtr Hit 15 1 bag(s) from #209
#    Preset[001:073] Gtr Hit 16 1 bag(s) from #210
#    Preset[001:074] Gtr Hit 17 1 bag(s) from #211
#    Preset[001:075] Gtr Hit 18 1 bag(s) from #212
#    Preset[001:076] Gtr Hit 19 1 bag(s) from #213
#    Preset[001:077] Gtr Hit 20 1 bag(s) from #214
#    Preset[001:078] Gtr Hit 21 1 bag(s) from #215
#    Preset[001:079] Gtr Hit 22 1 bag(s) from #216
#    Preset[001:080] Gtr Hit 23 1 bag(s) from #217
#    Preset[001:081] Gtr Hit 24 1 bag(s) from #218
#    Preset[001:082] Gtr Hit 25 1 bag(s) from #219
#    Preset[001:083] Gtr Hit 26 1 bag(s) from #220
#    Preset[001:084] Gtr Hit 27 1 bag(s) from #221
#    Preset[001:085] Gtr Hit 28 1 bag(s) from #222
#    Preset[001:086] Gtr Hit 29 1 bag(s) from #223
#    Preset[001:087] Gtr Hit 30 1 bag(s) from #224
#    Preset[001:088] Bass Hit 1 1 bag(s) from #225
#    Preset[001:089] Bass Hit 2 1 bag(s) from #226
#    Preset[001:090] Bass Hit 3 1 bag(s) from #227
#    Preset[001:091] Bass Hit 4 1 bag(s) from #228
#    Preset[001:092] Bass Hit 5 1 bag(s) from #229
#    Preset[001:093] Vox Hit 1 1 bag(s) from #230
#    Preset[001:094] Vox Hit 2 1 bag(s) from #231
#    Preset[001:095] Vox Hit 3 1 bag(s) from #232
#    Preset[001:096] Vox Hit 4 1 bag(s) from #233
#    Preset[001:097] Vox Hit 5 1 bag(s) from #234
#    Preset[001:098] Vox Hit 6 1 bag(s) from #235
#    Preset[001:099] Scratch 1 1 bag(s) from #236
#    Preset[001:100] Scratch 2 1 bag(s) from #237
#    Preset[001:101] Scratch 3 1 bag(s) from #238
#    Preset[001:102] Scratch 4 1 bag(s) from #239
#    Preset[001:103] Scratch 5 1 bag(s) from #240
#    Preset[001:104] Scratch 6 1 bag(s) from #241
#    Preset[001:105] Scratch 7 1 bag(s) from #242
#    Preset[001:106] Scratch 8 1 bag(s) from #243
#    Preset[001:107] Scratch 9 1 bag(s) from #244
#    Preset[001:108] Scratch 10 1 bag(s) from #245
#    Preset[001:109] Scratch 11 1 bag(s) from #246
#    Preset[001:110] Scratch 12 1 bag(s) from #247
#    Preset[001:111] Scratch 13 1 bag(s) from #248
#    Preset[001:112] Scratch 14 1 bag(s) from #249
#    Preset[001:113] Scratch 15 1 bag(s) from #250
#    Preset[001:114] Scratch 16 1 bag(s) from #251
#    Preset[001:115] Scratch 17 1 bag(s) from #252
#

MAX_TEMPO = 90
MIN_TEMPO = 60

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


def print_session_info(current_session):
    current_session.print_family_tree()
    current_session.print_available_midi_output_devices()
    current_session.print_available_midi_input_devices()
    current_session.print_default_soundfont_presets()
    print(current_session.tempo)


def get_session(tempo=120, name=None) -> Session:
    if name:
        playback_settings.recording_file_path = name
    s = Session(default_soundfont=SOUNDFONT)
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


def main():
    def setup(new_parts):
        if new_parts:
            parts_list = "_".join([part["name"] for part in new_parts.values()])
            tempo = int(uniform(MIN_TEMPO, MAX_TEMPO))
            filename = f"{datetime.now().isoformat()}_{parts_list}_{tempo}BPM.wav"
            main_session = get_session(tempo, filename)
            # print_session_info(main_session)
            for key, val in new_parts.items():
                new_parts[key]["part"] = main_session.new_part(new_parts[key]["name"])

    def intro():
        print(f"\rIntro", end="")
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

    def section_a():
        print(f"\rSection A", end="")

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
        bass.play_note(48, 1 / 8, random.uniform(1 / 8, 3 / 8), blocking=False)
        if choice([True, False]):
            drum_kit.play_note(snare(), 3 / 4, 1 / 4, blocking=False)
        drum_kit.play_note(hat(), 3 / 4, 1 / 4)

        print(f" 4", end="")
        drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
        if choice([True, False]):
            drum_kit.play_note(kick(), 1 / 4, 1 / 4, blocking=False)
        if choice([True, False]):
            scratch.play_note(72, 1 / 8, 1 / 4, blocking=False)
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

    def section_b():
        print(f"\rSection B", end="")

        print(f" 1", end="")
        bass.play_note(60, 1 / 8, random.uniform(3 / 4, 1), blocking=False)
        drum_kit.play_note(kick(), 2 / 4, 1, blocking=False)
        drum_kit.play_note(OPEN_HAT, 3 / 4, 1 / 2, blocking=False)
        scratch.play_note(72, 8 / 8, 1 / 4, blocking=False)
        drum_kit.play_note(ride(), random.random(), 1 / 4)
        drum_kit.play_note(ride(), random.random(), 1 / 4)

        drum_kit.play_note(ride(), random.random(), 1 / 4)
        drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
        drum_kit.play_note(ride(), random.random(), 1 / 4)

        print(f" 2", end="")
        scratch.play_note(72, 8 / 8, 1 / 2, blocking=False)
        drum_kit.play_note(ride(), random.random(), 1 / 4)
        drum_kit.play_note(ride(), random.random(), 1 / 4)

        bass.play_note(59, 1 / 8, random.uniform(1 / 4, 3 / 4), blocking=False)
        drum_kit.play_note(kick(), 2 / 4, 1, blocking=False)
        scratch.play_note(75, 8 / 8, 1 / 4, blocking=False)
        drum_kit.play_note(ride(), random.random(), 1 / 4)
        drum_kit.play_note(ride(), random.random(), 1 / 4)

        print(f" 3", end="")
        drum_kit.play_note(hat(), 3 / 4, 1 / 2, blocking=False)
        drum_kit.play_note(ride(), random.random(), 1 / 4)
        drum_kit.play_note(ride(), random.random(), 1 / 4)

        bass.play_note(58, 1 / 8, random.uniform(3 / 8, 5 / 8), blocking=False)
        drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
        scratch.play_note(72, 8 / 8, 1 / 2, blocking=False)
        drum_kit.play_note(ride(), random.random(), 1 / 4)
        drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
        drum_kit.play_note(ride(), random.random(), 1 / 4)

        print(f" 4", end="")
        bass.play_note(57, 1 / 8, random.uniform(3 / 8, 5 / 8), blocking=False)
        drum_kit.play_note(kick(), 2 / 4, 1, blocking=False)
        drum_kit.play_note(crash(), random.random(), 1 / 4)
        drum_kit.play_note(ride(), random.random(), 1 / 4)

        bass.play_note(56, 1 / 8, 1 / 2, blocking=False)
        drum_kit.play_note(ride(), random.random(), 1 / 4)
        drum_kit.play_note(snare(), 3 / 4, 1 / 2, blocking=False)
        scratch.play_note(78, 8 / 8, 1 / 2, blocking=False)
        drum_kit.play_note(ride(), random.random(), 1 / 4)

    def outro():
        print(f"\rOutro", end="")

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

    parts = {
        "drum_kit": {"name": f"Kit {choice(DRUM_KITS_I_LIKE)}"},
        "scratch": {"name": f"Scratch {choice(SCRATCH_KITS_I_LIKE)}"},
        "bass": {"name": f"Fat SynBass"},
    }

    setup(parts)

    drum_kit = parts["drum_kit"]["part"]
    scratch = parts["scratch"]["part"]
    bass = parts["bass"]["part"]

    intro()
    for _ in range(REPS):
        for _ in range(SECTION_A_REPS):
            section_a()
        for _ in range(SECTION_B_REPS):
            section_b()
    for _ in range(SECTION_A_REPS // 2):
        section_a()
    outro()


if __name__ == '__main__':
    main()
