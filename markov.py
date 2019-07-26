import numpy as np
import random as rm
import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 3001)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
# The statespace
states = ["G","A","B"]

# Possible sequences of events
transitionName = [["GG","GB","GA"],["BG","BB","BA"],["AG","AB","AA"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

while True:
     # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # A function that implements the Markov model to forecast the state/mood.
        def activity_forecast(notes):
            ran = rm.randint(1,4)
            if ran == 1:
                currentNote = "G"
            elif ran == 2:
                currentNote = "A"
            else:
                currentNote = "B"
            print("Start note: " + currentNote)
            # Shall store the sequence of states taken. So, this only has the starting state for now.
            #noteList = [noteI]
            i = 0
            # To calculate the probability of the activityList
            prob = 1
            while i != (notes):
                if currentNote == "G":
                    change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
                    if change == "GG":
                        prob = prob * 0.2
                        connection.send(bytes([3]))
                        pass
                    elif change == "GB":
                        prob = prob * 0.6
                        currentNote = "B"
                    
                    else:
                        prob = prob * 0.2
                        currentNote = "A"
                        
                elif currentNote == "B":
                    change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
                    if change == "BB":
                        prob = prob * 0.5
                        
                        pass
                    elif change == "BG":
                        prob = prob * 0.2
                        currentNote = "G"
                        
                    else:
                        prob = prob * 0.3
                        currentNote = "A"
                        
                elif currentNote == "A":
                    change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
                    if change == "AA":
                        prob = prob * 0.1
                        
                        pass
                    elif change == "AG":
                        prob = prob * 0.2
                        currentNote = "G"
                        
                    else:
                        prob = prob * 0.7
                        currentNote = "B"
                        
                    ran = rm.randint(1,4)
                    if ran == 1:
                        currentNote = "G"
                    elif ran == 2:
                        currentNote = "A"
                    else:
                        currentNote = "B"
                i += 1
                ran = rm.randint(1,4)
                if ran == 1:
                    currentNote = "G"
                elif ran == 2:
                    currentNote = "A"
                else:
                    currentNote = "B"
                
           

        # Function that forecasts the possible state for the next 2 days
        activity_forecast(20)
    finally:
        # Clean up the connection
        connection.close()
