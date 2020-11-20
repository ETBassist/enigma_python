class KeyGenerator:
    def make_cipher(self, digits, date):
        result = []
        keys = self.make_key(digits)
        offsets = self.make_offsets(date)
        for key, offset in zip(keys, offsets):
            result.append(key + offset)
        return result

    def make_offsets(self, date):
        squared = int(date) ** 2
        digits = list(map(int, str(squared)))
        return digits[-4:]

    def make_key(self, digits):
        result = []
        for i in range(len(digits) - 1):
            result.append(digits[i] + digits[i + 1])
        result = list(map(int, result))
        return result
