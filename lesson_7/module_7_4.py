team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print('В команде Мастера кода участников: %s !' % team1_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} c !".format(team1_time))
print(f"Команды решили {score_1} и {score_2} задач.")
print(challenge_result)
print(
    f"Сегодня было решено {score_1 + score_2} задач, в среднем по {round((team1_time + team2_time) / (score_1 + score_2), 1)} секунды на задачу!.")