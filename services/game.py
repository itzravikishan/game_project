import random

def play_game():
    choices = ['stone', 'paper', 'scissors']

    user = input('Enter stone/paper/scissors: ').lower()
    computer = random.choice(choices)

    print('Computer chose:', computer)

    if user == computer:
        print('Draw')
    elif (user == 'stone' and computer == 'scissors') or \
         (user == 'paper' and computer == 'stone') or \
         (user == 'scissors' and computer == 'paper'):
        print('You Win')
    else:
        print('You Lose')