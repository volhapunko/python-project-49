from random import randint

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 50


def is_even(number):
    return number % 2 == 0


def generate_number():
    random_number = randint(START, END)
    question = str(random_number)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer