# n означает, сколько игр будет сыграно
from typing import Any

n = int(input())
# создаем пустой список для всех игр
list_game = []
for i in range(n):
    list_current = [x for x in input().split(';')]
    list_game.append(list_current)
# Спартак;9;Зенит;10, Локомотив;12;Зенит;3, Спартак;8;Локомотив;15

# [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12', 'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]
# Всего игр можно не посчитать. Оно равно n - 1
# прочитал комменты к задаче. Вроде надо использовать словари


# Надо сначала перевести строки в список. Сравнить. И если спартак победил, то сохранить его в словарь. там будет
# спартак и value будет 3(ну потому что победа), и соответственно у его соперника будет 0
# надо определить победителя и проигравшего
# проверяем каждый список(т.е. каждую игру)

# создаем пустой словарь
teams_dict = {}
# Создаем словарь с ключами и вместо значения очков ставим 0
for i in list_game:
    for j in range(0, 3, 2):
        teams_dict[i[j]] = [0 for x in range(5)]


# Обращаемcя к каждому подсписку в списке list_game
for i in range(n):
    first_team_key = list_game[i][0]
    second_team_key = list_game[i][2]
    # будем определять победителя и добавлять значения в словарь.
    # key = имя команды, value = тут уже могут быть много разных значении, их будем просто друг за другом добавлять
    if int(list_game[i][1]) > int(list_game[i][3]):
        teams_dict[first_team_key][4] += 3
        teams_dict[second_team_key][4] += 0
        # Всего игр
        teams_dict[first_team_key][0] += 1
        teams_dict[second_team_key][0] += 1
        # Побед и поражении 1 и 3 индексы
        teams_dict[first_team_key][1] += 1
        teams_dict[second_team_key][3] += 1
    elif int(list_game[i][1]) == int(list_game[i][3]):
        teams_dict[first_team_key][4] += 1
        teams_dict[second_team_key][4] += 1
        # Всего игр
        teams_dict[first_team_key][0] += 1
        teams_dict[second_team_key][0] += 1
        # Ничьих
        teams_dict[first_team_key][2] += 1
        teams_dict[second_team_key][2] += 1
    else:
        teams_dict[first_team_key][4] += 0
        teams_dict[second_team_key][4] += 3
        # Всего игр
        teams_dict[first_team_key][0] += 1
        teams_dict[second_team_key][0] += 1
        # Побед и поражении 1 и 3 индексы
        teams_dict[first_team_key][3] += 1
        teams_dict[second_team_key][1] += 1
for k, w in teams_dict.items():
    print((k + ':'), *w, end='\n')
