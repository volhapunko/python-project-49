from random import choice, randint


def generate_operation():
    operations = ['+', '-', '*']
    return choice(operations)


def generate_number():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
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
