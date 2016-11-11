# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random


def number_to_name(number):
    # fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print('Error! Number is not in the correct range.')

        # convert number to a name using if/elif/else
        # don't forget to return the result!


def name_to_number(name):
    # fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print('Error! Name does not match.')

        # convert name to number using if/elif/else
        # don't forget to return the result!


def rpsls(name):
    # fill in your code below
    name = input('enter name :')
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5

    # use if/elif/else to determine winner
    if difference == 0:
        results = 'Player and computer tie!'
    elif difference >= 3:
        results = 'Computer wins!'
    elif difference <= 2:
        results = 'Player wins!'

    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)

    # print results
    print('\n')
    print("Player chooses " + name)
    print("Computer chooses " + comp_name)
    print(results)


# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")