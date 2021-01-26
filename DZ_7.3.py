class Cell:
    def __init__(self, unit):
        self.unit = int(unit)

    def __add__(self, other):
        return Cell(self.unit + other.unit)

    def __sub__(self, other):
        if self.unit - other.unit > 0:
            return Cell(self.unit - other.unit)

    def __mul__(self, other):
        return Cell(self.unit * other.unit)

    def __truediv__(self, other):
        return Cell(self.unit // other.unit)

    def make_oder(self, number_unit):
        number_row = self.unit // number_unit
        remain = self.unit - number_row*number_unit
        my_str = f'{number_unit*"*"}\n'*number_row + remain*'*'
        print(my_str)

cell_1 = Cell(25)
cell_2 = Cell(10)
cell_3 = cell_1 + cell_2
cell_4 = cell_1 - cell_2
cell_5 = cell_1 * cell_2
cell_6 = cell_1 / cell_2

print(cell_3.unit, cell_4.unit, cell_5.unit, cell_6.unit)

cell_1.make_oder(3)