class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return ('Машина поехала')

    def stop(self):
        return ('Машина остановилась')

    def turn(self, direction):
        return (f'Машина повернула на {direction}')

    def show_speed(self):
        return (f'Текущая скорость автомобиля: {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Превышение допустимой скорости')
        return (f'Текущая скорость автомобиля: {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name, acceleration, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.acceleration = acceleration

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение допустимой скорости')
        return (f'Текущая скорость автомобиля: {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=True)


car_1 = TownCar(30, 'gray', 'VAZ-2114')
car_2 = SportCar(100, 'red', 'Marusia', 20)
car_3 = WorkCar(80, 'blue', 'GAZ-3302')
car_4 = PoliceCar(50, 'white', 'VAZ-2110')

list_avto = [car_1, car_2, car_3, car_4]
for i in list_avto:
    print(i.speed)
    print(i.color)
    print(i.name)
    print(i.is_police)
    try:
        print(i.acceleration)
    except:
        pass
    print(i.stop())
    print(i.turn('лево'))
    print(i.show_speed())




