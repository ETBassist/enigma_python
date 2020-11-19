class Rotator:
    def rotate(self, array, steps):
        for i in range(steps):
            element = array.pop(0)
            array.append(element)
        return array
