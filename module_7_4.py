def search_result():
    if (score_1 > score_2 or
        score_1 == score_2 and
        team1_time > team2_time):
        return f'Результат битвы: победа команды {team1_name}!'
    elif (score_1 < score_2 or
          score_1 == score_2 and
          team1_time < team2_time):
        return f'Результат битвы: победа команды {team2_name}!'
    else:
        return f'Ничья!'


team1_name = 'Мастера кода'
team1_num = 5
score_1 = 40
team2_name = 'Волшебники данных'
team1_time = 10717.6
team2_num = 6
score_2 = 42
team2_time = 18015.2
tasks_total = score_1 + score_2
time_avg = round(
    (team1_time + team2_time) / tasks_total,
    1
    )
challenge_result = search_result()

print(
    'В команде %(team_name)s участников: %(team_num)d!'
    %{'team_name': team1_name, 'team_num': team1_num}
    )
print(
    'В команде %(team_name)s участников: %(team_num)d!'
    %{'team_name': team2_name, 'team_num': team2_num}
    )
print(
    'Итого сегодня в командах участников: %(team1_num)d и %(team2_num)d'
    %{'team1_num': team1_num, 'team2_num': team2_num}
    )
print('-' * 60)
print(
    'Команда {team_name} решила задач: {team_score}!'.format(
        team_name=team1_name, team_score=score_1
        )
    )
print(
    '{team_name} решили задачи за {team_time} с!'.format(
        team_name=team1_name, team_time=team1_time
        )
    )
print(
    'Команда {team_name} решила задач: {team_score}!'.format(
        team_name=team2_name, team_score=score_2
        )
    )
print(
    '{team_name} решили задачи за {team_time} с!'.format(
        team_name=team2_name, team_time=team2_time
        )
    )
print('-' * 60)
print(f'Команды решили {score_1} и {score_2} задач.')
print(challenge_result)
print(
    f'Сегодня было решено {tasks_total} задач,'
    f'в среднем по {time_avg} секунды на задачу!'
    )