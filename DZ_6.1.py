from itertools import cycle
from time import sleep

class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running():
        for i in cycle(['красный', 'желтый', 'зеленый']):
            if i == 'красный':
                print(i)
                sleep(7)
            elif i == 'желтый':
                print(i)
                sleep(2)
            elif i == 'зеленый':
                print(i)
                sleep(7)

trafficlights1 = TrafficLight

trafficlights1.running()