from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def generate_operation():
    operations = ['+', '-', '*']
    return choice(operations)


def generate_quest_and_answer():
    start = 1
    end = 10
    number1 = randint(start, end)
    number2 = randint(start, end)
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
