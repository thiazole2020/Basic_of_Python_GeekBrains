class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Полный заработок сотрудника: {self._income["wage"] + self._income["bonus"]}')


worker_1 = Position('Aleksander', 'Petrov', 'Director', 100000, 20000)

print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)
print(worker_1._income)
print(worker_1.get_full_name())
print(worker_1.get_total_income())




