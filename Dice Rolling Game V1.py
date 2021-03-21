""""
Version 1

This version allows 2/3 players to input their player names and this is the only action required of the players.
The program then randomly outputs each players scores as in a 6 faced dice.
When there are two top players the program continues with another round of the game considering only the top players.
The program stops when there is a winner (player with the highest score).

"""

import random


no_users = int(input('how many players'))
if no_users == 2:
    user1 = input('user1');user2 = input('user2')
    while True:
        user1_no = random.randint(1,6)
        user2_no = random.randint(1,6)
        if user1_no == user2_no:
            print(f'Both players have {user1_no}')
            print("Rolling again ...")
            continue
        elif user1_no < user2_no:
            print(f"{user1}'s die showed {user1_no} and {user2}'s die showed {user2_no} ")
            print(f'{user2} is the Winner')
            break
        elif user1_no > user2_no:
            print(f"{user1}'s number is {user1_no} and {user2}'s number is {user2_no} ")
            print(f'{user1} is the Winner')
            break
elif no_users == 3:
    user1 = input('user1');user2 = input('user2');user3 = input('user3')
    while True:
        user1_no = random.randint(1,6)
        user2_no = random.randint(1,6)
        user3_no = random.randint(1,6)
        if (user1_no == user2_no) and (user2_no == user3_no):
            print(f"all three players have{user3_no}")
            print("Rolling again ...")
            continue
        elif (user1_no > user2_no) and (user1_no > user3_no):
            print(f"{user1}'s die showed {user1_no}, {user2}'s die showed {user2_no} and {user3}'s die showed {user3_no} ")
            print(f'{user1} is the Winner')
            break
        elif (user2_no > user1_no) and (user2_no > user3_no):
            print(f"{user1}'s die showed {user1_no}, {user2}'s die showed {user2_no} and {user3}'s die showed {user3_no} ")
            print(f'{user2} is the Winner')
            break
        elif (user3_no > user1_no) and (user3_no > user2_no) :
            print(f"{user1}'s die showed {user1_no}, {user2}'s die showed {user2_no} and {user3}'s die showed {user3_no} ")
            print(f'{user3} is the Winner')
            break
        elif (user1_no == user2_no) and (user1_no > user3_no):
            print(f"{user1}'s die showed {user1_no}, {user2}'s die showed {user2_no} and {user3}'s die showed {user3_no} ")
            print(f"{user3} is out")
            print("Rolling again ...")
            while True:
                user1_no = random.randint(1,6);user2_no = random.randint(1,6)
                if user1_no == user2_no:
                    print(f'Both {user1} and {user2} have {user1_no}')
                    print("Rolling again ...")
                    continue
                elif user1_no < user2_no:
                    print(f"{user1}'s die showed {user1_no} and {user2}'s die showed {user2_no} ")
                    print(f'{user2} is the Winner')
                    break
                elif user1_no > user2_no:
                    print(f"{user1}'s number is {user1_no} and {user2}'s number is {user2_no} ")
                    print(f'{user1} is the Winner')
                    break
            break
        elif (user1_no == user3_no) and (user1_no > user2_no):
            print(f"{user1}'s die showed {user1_no}, {user2}'s die showed {user2_no} and {user3}'s die showed {user3_no} ")
            print(f"{user2} is out")
            print("Rolling again ...")
            while True:
                user1_no = random.randint(1, 6);user3_no = random.randint(1, 6)
                if user1_no == user3_no:
                    print(f'Both {user1} and {user3} have {user1_no} ')
                    print("Rolling again ...")
                    continue
                elif user1_no < user3_no:
                    print(f"{user1}'s die showed {user1_no} and {user3}'s die showed {user3_no} ")
                    print(f'{user3} is the Winner')
                    break
                elif user1_no > user3_no:
                    print(f"{user1}'s number is {user1_no} and {user3}'s number is {user3_no} ")
                    print(f'{user1} is the Winner')
                    break
            break
        elif (user2_no == user3_no) and (user2_no > user1_no):
            print(f"{user1}'s die showed {user1_no}, {user2}'s die showed {user2_no} and {user3}'s die showed {user3_no} ")
            print(f"{user1} is out")
            print("Rolling again ...")
            while True:
                user2_no = random.randint(1, 6);user3_no = random.randint(1, 6)
                if user2_no == user3_no:
                    print(f'Both{user2} and {user3} have {user2_no} ')
                    print("Rolling again ...")
                    continue
                elif user2_no < user3_no:
                    print(f"{user2}'s die showed {user2_no} and {user3}'s die showed {user3_no} ")
                    print(f'{user3} is the Winner')
                    break
                elif user2_no > user3_no:
                    print(f"{user2}'s number is {user2_no} and {user3}'s number is {user3_no} ")
                    print(f'{user2} is the Winner')
                    break
            break
else:
    print('players must be at least 2 and at most 3')








