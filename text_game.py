"""min 200 lines of code."""
# text game
import random
print('------------------------------------')
print('------- WELCOME TO ZOMBIELAND ------')
print('------------------------------------')
print('You stand on the road and you see '
      'a huge number of zombies.  ')
print('')
weapon = 0 # you don't have any weapon
health = 100 # 100%

choise_1 = input('You see a car. Will you take it? [Y/N] : ')
print('')

# you take a car
lst_yes = ['y', 'Y', 'Yes', 'YES', 'yes']
lst_not = ['n', 'N', 'Not', 'NOT', 'No', 'NO', 'not', 'no']

if choise_1 in lst_yes:
    print('ZOMBIE ATE YOUR BRAINS !!! um,um,um.... ')
    print('RULE #31 CHECK THE BACK SEAT')
    print('')
# you don't take a car
elif choise_1 in lst_not:
    print('You decided to run. RULE #1 CARDIO')
    print('')
else:
    print('Don\'t waste your time yes or not')
    print('')
# gas station
print('You run 5 km and see a gas station')
print('')
print('There may be supplies. You go inside ')
print('')
print('There is a chainsaw in front of you')
print('')
choise_2 = input('Will you take it? [Y/N] : ')
print('')

#you take a chainsaw
if choise_2 in lst_yes:
    print("Now you have a chainsaw ")
    weapon += 1
    print('')

#you don't take a chainsaw
else:
    print('Maybe you are a Kung-Fu Master')
    print('')
#zombie attak
zombie_health = 200

print('When you went outside, one of those crazy zombies attaks you ')
print('')
choise_3 = input('Try to kick him? [Y/N] : ')
print('')

# you fight
if choise_3 in lst_yes:
    print("    You decided to fight   ")
    print('---------------------------')
    print('----- Zombie Massacre -----')
    print('---------------------------')

    # you have a weapon
    if weapon >= 1:
        while health > 0 and zombie_health > 0:

            your_strike = int(random.randint(40,80))
            print('You strike {} points with a chainsaw'.format(your_strike))
            zombie_health -= your_strike
            zombi_strike = int(random.randint(10,20))
            print('Zombie strikes {} points back'.format(zombi_strike))
            health -= zombi_strike
            print('')
            continue
        if zombie_health <= 0:
                print('YOU KILLED THOSE PEICE OF SHIT !!! ')
                print('---------------------------------- ')
                print('---------- YOU WIN --------------- ')
        else:
                print('ZOMBIE ATE YOUR BRAINS !!! um,um,um.... ')

    # you don't have a weapon
    else:
        while health > 0 and zombie_health > 0:

            your_strike = int(random.randint(10, 20))
            print('You strike {} points with a Kung Fu'.format(your_strike))
            zombie_health -= your_strike
            zombi_strike = int(random.randint(10, 20))
            print('Zombie strikes {} points back'.format(zombi_strike))
            health -= zombi_strike
            print('')
            continue
        if zombie_health <= 0:
            print('YOU KILLED THOSE PEICE OF SHIT !!! ')
            print('---------------------------------- ')
            print('---------- YOU WIN --------------- ')
        else:
            print('ZOMBIE ATE YOUR BRAINS !!! um,um,um.... ')
            print('------------------------')
            print('RULE #4 DON\'T BE A HERO')

# you try to escape
else:
    print('You  escaped  the danger')
    print('------------------------')
    print('RULE #4 DON\'T BE A HERO')










