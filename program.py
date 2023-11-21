from functions import question, statistics
import requests
from random import shuffle

response = requests.get('https://www.jsonkeeper.com/b/ULHH')
profile = response.json()

questions = question(profile)
shuffle(questions)

for que in questions:
    print('\n' + que.build_question())
    user_response = input()
    que.user_response = user_response
    que.is_correct()
    if que.is_correct():
        que.get_points()
    print(que.feedback())


if __name__ == '__main__':
    print(statistics(questions))