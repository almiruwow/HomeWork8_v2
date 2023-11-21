class Question:
    def __init__(self, question_text, complexity, correct_answer):
        self.question_text = question_text
        self.complexity = complexity
        self.correct_answer = correct_answer
        self.count = 0
        self.asked = False
        self.user_response = None

    def get_points(self):
        self.count = int(self.complexity) * 10

    def is_correct(self):
        if self.user_response == self.correct_answer:
            return True
        return False

    def build_question(self):
        return f'Вопрос: {self.question_text}\nСложность {self.complexity}/5'

    def feedback(self):
        if self.is_correct():
            self.asked = True
            return f'Ответ верный, получено {self.count} баллов'
        elif not self.is_correct():
            return f'Ответ неверный, верный ответ {self.correct_answer}'
