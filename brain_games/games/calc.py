from random import choice, randint

GAME_DESCRIPTION = 'What is the result of the expression?'
START = 1
END = 50


def generate_operation():
    operations = ['+', '-', '*']
    return choice(operations)


def generate_number():
    number1 = randint(START, END)
    number2 = randint(START, END)
    operation = generate_operation()
    question = (f'{number1} {operation} {number2}')

    if operation == '+':
        correct_answer = number1 + number2
    elif operation == '-':
        correct_answer = number1 - number2
    elif operation == '*':
        correct_answer = number1 * number2
    correct_answer = str(correct_answer)
    
    return question, correct_answer
