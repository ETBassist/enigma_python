class Rotator:
    def left_rotate(self, array, steps):
        for i in range(steps):
            array.append(array.pop(0))
        return array

    def right_rotate(self, array, steps):
        for i in range(steps):
            array.insert(0, array.pop(-1))
        return array
