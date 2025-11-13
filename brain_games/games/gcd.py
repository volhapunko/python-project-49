from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_number():
    start = 1
    end = 100
    number1 = randint(start, end)
    number2 = randint(start, end)
    question = (f'{number1} {number2}')
    a, b = number1, number2

    while b != 0:
        a, b = b, a % b
    
    correct_answer = str(a)

    return question, correct_answer