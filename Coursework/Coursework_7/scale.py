class Scale:
    maj_offsets = {
        0: 0,
        1: 2,
        2: 4,
        3: 5,
        4: 7,
        5: 9,
        6: 11,
    }

    def __init__(self, tonic):
        self._tonic = tonic

    def __getitem__(self, item):
        return self.note(item)

    def note(self, interval):
        interval -= 1
        note = self._tonic + self.maj_offsets[interval % 7] + 12 * (interval // 7)
        # print(note)
        return note
