from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
START = 1
END = 100


def generate_number():
    number1 = randint(START, END)
    number2 = randint(START, END)
    question = (f'{number1} {number2}')
    a, b = number1, number2

    while b != 0:
        a, b = b, a % b
    
    correct_answer = str(a)

    return question, correct_answer