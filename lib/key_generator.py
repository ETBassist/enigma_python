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
        result.append(digits[0] + digits[1])
        result.append(digits[1] + digits[2])
        result.append(digits[2] + digits[3])
        result.append(digits[3] + digits[4])
        result = list(map(int, result))
        return result
