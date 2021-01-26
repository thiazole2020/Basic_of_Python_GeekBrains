class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки...')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ({self.title})...')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ({self.title})...')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ({self.title})...')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

for i in [pen, pencil, handle]:
    i.draw()

