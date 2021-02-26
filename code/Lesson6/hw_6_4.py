class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'{self.name}: текущая скорость {self.speed}'


class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.max_speed:
            return f'{self.name} превышение скорости!'
        else:
            return f'{self.name} - дозволительная скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(TownCar):
    max_speed = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


vesta = TownCar(60, 'Blue', 'Vesta', False)
mersedes = SportCar(130, 'Red', 'Mercedes', False)
gaz = WorkCar(50, 'Gray', 'GAZ', False)
ford = PoliceCar(80, 'White', 'Ford', True)
print(vesta.show_speed())
print(gaz.show_speed())
print(f'Марка: {ford.name}, цвет: {ford.color}')
print(f'{ford.name} - Полиция? {ford.is_police}')
print(f'{mersedes.name} - это Полиция? {mersedes.is_police}')
print(f'{gaz.turn_left()}, а {vesta.turn_right()}')

