# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random
import numpy as np

counts = {}

def player(prev_play, opponent_history=[]):
    global counts

    #Detect new player:
    if (prev_play == ""):
        opponent_history = []
        counts = {}

    #Update move history:
    opponent_history.append(prev_play)

    #Default move guess:
    guess = "R"

    #How many previous moves to consider:
    memory = 5

    if len(opponent_history) >= memory:
        #Accumulate move pattern counts:
        moves = opponent_history[-memory:]
        move_string = "".join(moves)

        if move_string not in counts:
            counts[move_string] = 1
        else:
            counts[move_string] += 1

        #Get most probable next move:
        moves = opponent_history[-(memory-1):]

        guesses = ["R", "P", "S"]

        options = ["".join(moves + [g]) for g in guesses]

        option_counts = []

        for op in options:
            if op in counts:
                option_counts.append(counts[op])
            else:
                option_counts.append(0)

        idx = np.argmax(option_counts)

        guess = guesses[idx]

    #Respond to the predicted move:
    response = {
        "R" : "P", "P" : "S", "S" : "R"
    }

    return response[guess]