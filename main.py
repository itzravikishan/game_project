from services.game import *

def game():
    while True:
        print('\n Game Menu')
        print('1.Play Game')
        print('2.Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            play_game()
        elif choice == 2:
            print('Thank You!')
            break
        else:
            print('Invalid choice')

game()