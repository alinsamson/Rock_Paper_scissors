from random import randint

play_options = ["Rock", "Paper", "Scissors"]

computer_option = play_options[randint(0,2)]

player = False

while player == False:
    player = input('Select your choice:')
    player = player.capitalize()
    if (player != "Rock") and (player != "Paper") and (player != "Scissors"):
        print('Your choice are wrong. Bye!')
        break
    else:
        if player == computer_option:
            print('Tie game!')
        elif player == "Rock":
            if computer_option == "Paper":
                print(f'You have lost. {computer_option} covers {player}.')
            else:
                print(f'You have won. {player} smashes {computer_option}.')
        elif player == "Paper":
            if computer_option == "Scissors":
                print(f'You have lost. {computer_option} cut {player}.')
            else:
                print(f'You have won. {player} covers {computer_option}.')
        elif player == "Scissors":
            if computer_option == "Rock":
                print(f'You have lost. {computer_option} smashes {player}.')
            else:
                print(f'You have won. {player} cut {computer_option}.')
player = False
computer_option = play_options[randint(0,2)]
