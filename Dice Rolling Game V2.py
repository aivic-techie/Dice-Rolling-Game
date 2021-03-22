"""
Version 2

This version allows two or more players.
The players input their names as a tuple to the game function and as with version 1 there is no further action required.
The program then randomly outputs each players scores as in a 6 faced dice.
When there are top players the program continues with another round of the game considering only the top players.
The program stops when there is a winner (player with the highest score).
"""

import numpy as np
    
    
def dice(atuple):
    '''To generate dice faces as integers
    and return players and their scores'''
    scores = {}
    s = np.random.randint(1, 7, len(atuple))
    for i, p in enumerate(atuple):
        scores[p] = s[i]
    return scores


def greater(bdict):
    '''To determine the greatest dice face'''
    # print(bdict)
    values = np.array(list(bdict.values()))
    max_score = np.max(values)
    maxs = np.where(values==max_score, 1, 0)
    names = np.array(list(bdict.keys()))
    arg = np.arange(1, len(names) + 1)
    T = (maxs * arg) - 1
    top = names[T[T>=0]]
    return top, max_score
    

def game(tuple_players):
    '''Players should be of class tuple'''
    assert type(tuple_players) == tuple
    results = dice(tuple_players)
    a, b = greater(results)
    if len(a)==1:
        print(results)
        print(f"The winner is: {a}")
        return None
        
    elif len(a) > 1:
        print(results)
        print(f"Players {a} have the same score {b}")
        final = {d:results[d] for d in tuple_players if d in a}
        print(f"{final}: Rolling again...\n")
        return game(tuple(final))


some_players = ("Froppy", "Uravity", "Duke", "Midnight",
     "Endeavor", "Nighteye", "Eraser_Head", "Tanjiro",
     "Nezuko", "Stain", "Invisible", "Nezu")
game(some_players) 
            









