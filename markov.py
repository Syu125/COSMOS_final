import numpy as np
import random as rm

# The statespace
states = ["G","A","B"]

# Possible sequences of events
transitionName = [["GG","GB","GA"],["BG","BB","BA"],["AG","AB","AA"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

# A function that implements the Markov model to forecast the state/mood.
def activity_forecast(notes):
    # Choose the starting state
    ran = random.int(1,4)
    if ran == 1:
        currentNote = "G"
    elif ran == 2:
        currentNote = "A"
    else:
        currentNote = "B"
            
    print("Start note: " + currentNote)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    noteList = [currentNote]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != notes:
        if currentNote == "G":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                noteList.append("G")
                pass
            elif change == "SR":
                prob = prob * 0.6
                currentNote = "B"
                noteList.append("B")
            else:
                prob = prob * 0.2
                currentNote = "A"
                noteList.append("A")
        elif currentNote == "B":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 0.5
                noteList.append("B")
                pass
            elif change == "RS":
                prob = prob * 0.2
                currentNote = "G"
                noteList.append("G")
            else:
                prob = prob * 0.3
                currentNote = "A"
                noteList.append("A")
        elif currentNote == "A":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "II":
                prob = prob * 0.1
                noteList.append("A")
                pass
            elif change == "IS":
                prob = prob * 0.2
                currentNote = "G"
                noteList.append("G")
            else:
                prob = prob * 0.7
                currentNote = "B"
                noteList.append("B")
        i += 1  
    print("Possible notes: " + str(noteList))
    print("End note after "+ str(notes) + " notes: " + currentNote)
    print("Probability of the possible sequence of notes: " + str(prob))

# Function that forecasts the possible state for the next 2 days
activity_forecast(2)
