class Road:
    def __init__(self, _length, _width, _mass_asf, _thickness):
        self._length = _length
        self._width = _width
        self._mass_asf = _mass_asf
        self._thickness = _thickness

    def mass_sum(self):
        return self._mass_asf * self._thickness * self._length * self._width


r = Road(100, 30, 25, 5)
print(f'Масса покрытия: {r.mass_sum()} кг.')






