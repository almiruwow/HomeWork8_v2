from main import Question


def question(profile):
    """
    Создаем экземпляры класса и возвращаем их в списке
    """
    q1 = Question(profile[0]['q'], profile[0]['d'], profile[0]['a'])
    q2 = Question(profile[1]['q'], profile[1]['d'], profile[1]['a'])
    q3 = Question(profile[2]['q'], profile[2]['d'], profile[2]['a'])
    q4 = Question(profile[3]['q'], profile[3]['d'], profile[3]['a'])
    q5 = Question(profile[4]['q'], profile[4]['d'], profile[4]['a'])
    questions = [q1, q2, q3, q4, q5]
    return questions


def statistics(lists):
    """
    Выводит статистику
    """
    total_points = 0
    answers = 0
    for count in lists:
        total_points += count.count
        if count.asked:
            answers += 1

    return f'\nВот и все!\n' \
           f'Отвечено на {answers} из {len(lists)}\n' \
           f'Набранно баллов: {total_points}'




