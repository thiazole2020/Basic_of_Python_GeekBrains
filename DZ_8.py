import random, copy, DZ8module

class LotoCard:
    def __init__(self, player):
        self.player_name = player
        self.card_number = DZ8module.generate_loto_card()

class LotoGame:
    def __init__(self, people, computer):
        self.people_name = people.player_name
        self.computer_name = computer.player_name
        self.player_number = copy.deepcopy(people.card_number)
        self.computer_number = copy.deepcopy(computer.card_number)
        self.number_cross_out_computer = 0
        self.number_cross_out_people = 0

    def start(self):
        barrel_list = list(range(1, 91))
        for i in range(1, 91):
            wrong_answer = False
            have_number = False
            DZ8module.loto_card_for_view(self.computer_number, self.computer_name)
            DZ8module.loto_card_for_view(self.player_number, self.people_name)
            current_barrel = random.choice(barrel_list)
            barrel_list.pop(barrel_list.index(current_barrel))
            print(f'Новый бочонок: {current_barrel}, осталось {len(barrel_list)}')
            while True:
                people_choice = input('Хотите зачеркнуть? y/n: ')
                if people_choice == 'y' or people_choice == 'n':
                    break
            for i in self.computer_number:
                for j in i:
                    if current_barrel == j:
                        index = self.computer_number[self.computer_number.index(i)].index(j)
                        self.computer_number[self.computer_number.index(i)].remove(j)
                        self.computer_number[self.computer_number.index(i)].insert(index, '--')
                        self.number_cross_out_computer += 1
            for i in self.player_number:
                for j in i:
                    if current_barrel == j and people_choice == 'y':
                        have_number = True
                        index = self.player_number[self.player_number.index(i)].index(j)
                        self.player_number[self.player_number.index(i)].remove(j)
                        self.player_number[self.player_number.index(i)].insert(index, '--')
                        self.number_cross_out_people += 1
                    elif current_barrel == j and people_choice == 'n':
                        have_number = True
                        wrong_answer = True
                        print(f'Вы не заметили число {current_barrel} в Вашей карточке!')
                        break
            if not have_number and people_choice == 'y':
                print(f'Вы захотели вычеркнуть число, которого нет в Вашей карточке.')
                wrong_answer = True
            if wrong_answer:
                print(f'Выйграл {self.computer_name}!')
                break
            if self.number_cross_out_computer == 15:
                if self.number_cross_out_computer == self.number_cross_out_people:
                    print(f'Выйграли оба игрока {self.computer_name} и {self.people_name}!')
                    break
                else:
                    print(f'Выйграл {self.computer_name}!')
                    break
            if self.number_cross_out_people == 15:
                if self.number_cross_out_computer == self.number_cross_out_people:
                    print(f'Выйграли оба игрока {self.computer_name} и {self.people_name}!')
                    break
                else:
                    print(f'Выйграл {self.people_name}!')
                    break

people = LotoCard('Человек')
computer = LotoCard('Компьютер')
game = LotoGame(people, computer)
game.start()


