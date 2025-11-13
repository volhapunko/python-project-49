from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression():
    start = randint(1, 10)
    length = randint(5, 10)
    step = randint(1, 5)
    
    progression = []
    for element in range(length):
        current_element = start + element * step
        progression.append(current_element)
    return (progression)


def generate_number():
    progression = generate_progression()
    skip_number = randint(0, len(progression) - 1)
    question = []
    for i in range(len(progression)):
        if i == skip_number:
            question.append('..')
        else:
            question.append(str(progression[i]))
    
    correct_answer = progression[skip_number]
    return ' '.join(question), str(correct_answer)