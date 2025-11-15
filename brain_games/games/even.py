from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_quest_and_answer():
    start = 1
    end = 50
    random_number = randint(start, end)
    question = str(random_number)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer