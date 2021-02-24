class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Объединение двух клеток: {self.quantity + other.quantity}'

    def __sub__(self, other):
        try:
            if self.quantity - other.quantity <= 0:
                raise ValueError
            else:
                return f'Клетка стала меньше: {self.quantity - other.quantity}'
        except ValueError:
            print('Операция не возможна')

    def __mul__(self, other):
        return f'Создаётся общая клетка: {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Создаётся клетка из деления: {self.quantity // other.quantity}'

    def make_order(self, row):
        ordered = ['*' * row for _ in range(self.quantity // row)]
        ordered.append('*' * (self.quantity % row))
        return f'\n'.join(ordered)


cell_1 = Cell(11)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print()
print(cell_2.make_order(5))
