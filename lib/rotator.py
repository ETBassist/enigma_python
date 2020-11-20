class Rotator:
    def right_rotate(self, array, steps):
        for i in range(steps):
            array.append(array.pop(0))
        return array
