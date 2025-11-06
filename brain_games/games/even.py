from random import randint


def is_even(number):
    return number % 2 == 0


def generate_number():
    random_number = randint(1, 100)
    question = str(random_number)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer