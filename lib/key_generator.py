class KeyGenerator:
    def make_offsets(self, date):
        squared = int(date) ** 2
        digits = list(map(int, str(squared)))
        return digits[-4:]
