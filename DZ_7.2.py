from abc import abstractmethod

class Clothes:
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return self.size*6.5 + 0.5

class Costume(Clothes):
    def __init__(self, height):
        self.size = height

    @property
    def consumption(self):
        return self.size*2 + 0.3

size_row = [10, 11, 12]                 #размерный ряд

coat = []
for i in size_row:
    coat.append(Coat(i))
print(coat[0].consumption)

costume = []
for i in size_row:
    costume.append(Costume(i))
print(costume[0].consumption)

clothes = []
for i in coat:
    clothes.append(i)
for i in costume:
    clothes.append(i)

sum_consumption = 0
for i in clothes:
    sum_consumption += i.consumption
print(sum_consumption)                      #суммарный расход ткани на все виды одежды

