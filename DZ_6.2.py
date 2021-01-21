class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        self.standartweight = 25    #норматив массы на 1 кв.м дороги толщиной 1 см, кг

    def weight(self, thickness):
        print(f'масса асфальта на дороге: {self._lenght*self._width*self.standartweight*thickness/1000} тонн')


road_1 = Road(10000, 10)

road_1.weight(5)