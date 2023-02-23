# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

idealResponse = {'P': 'S', 'R': 'P', 'S': 'R'}
options = ["R", "P", "S"]

def player(prev_play, opponent_history: list=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    else: # new oponent
        opponent_history = []

    if (len(opponent_history) < 4): # not enough history to make prediction
        return idealResponse[options[random.randint(0,2)]]

    # join last 4 plays by index
    lastPlays = [ ''.join(opponent_history[k:k+4]) for k, v in enumerate(opponent_history[:-3]) ]
    
    # remove oldest and add possible next play    
    nextPlays = [ ''.join([ *opponent_history[-3:], v ]) for v in options] 

    # count repeated plays to find a pattern
    sub_order = { k: lastPlays.count(k) for k in nextPlays } 
    
    # get most repeated play, then get the potential next play
    prediction = max(sub_order, key=sub_order.get)[-1]
    
    return idealResponse[prediction]



