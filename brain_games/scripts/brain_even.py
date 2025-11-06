import prompt

from brain_games.cli import welcome_user
from brain_games.games.even import generate_number


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    rounds_to_win = 3

    for round in range(rounds_to_win):
        question, correct_answer = generate_number()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
        print('Correct!')
    
    print(f'Congratulations, {name}!')

    
if __name__ == '__main__':
    main()