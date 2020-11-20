class Rotator:
    def rotate(self, array, steps, direction):
        if direction == 'left':
            return self.left_rotate(array, steps)
        return self.right_rotate(array, steps)

    def left_rotate(self, array, steps):
        for i in range(steps):
            array.append(array.pop(0))
        return array

    def right_rotate(self, array, steps):
        for i in range(steps):
            array.insert(0, array.pop(-1))
        return array
