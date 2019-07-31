import threading
import numpy as np
import random as rm

def piece(notes):
    
    states = ["C","D","E","F","G","A","B","C2"]
    result = []
    final = []

    # Possible sequences of events
    transitionName = [["CC","CD","CE","CF","CG","CA","CB","CC2"],["DC","DD","DE","DF","DG","DA","DB","DC2"],["EC","ED","EE","EF","EG","EA","EB","EC2"],["FC","FD","FE","FF","FG","FA","FB","FC2"],["GC","GD","GE","GF","GG","GA","GB","GC2"],["AC","AD","AE","AF","AG","AA","AB","AC2"],["BC","BD","BE","BF","BG","BA","BB","BC2"],["C2C","C2D","C2E","C2F","C2G","C2A","C2B","C2C2"]]

    # Probabilities matrix (transition matrix)
    transitionMatrix = [[0.1,0.2,0.1,0.1,0.1,0.2,0.1,0.1],[0.1,0.1,0.1,0.2,0.1,0.1,0.1,0.2],[0.1,0.1,0.3,0.1,0.1,0.1,0.1,0.1],[0.1,0.1,0.2,0.2,0.1,0.1,0.1,0.1],[0.1,0.1,0.1,0.1,0.1,0.1,0.3,0.1],[0.2,0.1,0.1,0.2,0.1,0.1,0.1,0.1],[0.1,0.3,0.1,0.1,0.1,0.1,0.1,0.1],[0.1,0.1,0.2,0.1,0.1,0.2,0.1,0.1]]
    ran = rm.randint(1,9)
    if ran == 1:
        currentNote = "C"
    elif ran == 2:
        currentNote = "D"
    elif ran == 3:
        currentNote = "E"
    elif ran == 4:
        currentNote = "F"
    elif ran == 5:
        currentNote = "G"
    elif ran == 6:
        currentNote = "A"
    elif ran == 7:
        currentNote = "B"    
    else:
        currentNote = "C2"
    print("Start note: " + currentNote)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    #noteList = [noteI]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != (notes):
        if currentNote == "C":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "CC":
                prob = prob * 0.1
                currentNote = "C"
                
            elif change == "CD":
                prob = prob * 0.2
                currentNote = "D"
                
            elif change == "CE":
                prob = prob * 0.1
                currentNote = "E"
                
            elif change == "CF":
                prob = prob * 0.1
                currentNote = "F"
                
            elif change == "CG":
                prob = prob * 0.1
                currentNote = "G"
                
            elif change == "CA":
                prob = prob * 0.2
                currentNote = "A"
                
            elif change == "CB":
                prob = prob * 0.1
                currentNote = "B"
                
            else:
                prob = prob * 0.1
                currentNote = "C2"
                
        elif currentNote == "D":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "DC":
                prob = prob * 0.1
                currentNote = "C"
                
            elif change == "DD":
                prob = prob * 0.2
                currentNote = "D"
                
            elif change == "DE":
                prob = prob * 0.1
                currentNote = "E"
                
            elif change == "DF":
                prob = prob * 0.1
                currentNote = "F"
                
            elif change == "DG":
                prob = prob * 0.1
                currentNote = "G"
                
            elif change == "DA":
                prob = prob * 0.2
                currentNote = "A"
                
            elif change == "DB":
                prob = prob * 0.1
                currentNote = "B"
                
            else:
                prob = prob * 0.1
                currentNote = "C2"
               
        elif currentNote == "E":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "EC":
                prob = prob * 0.1
                currentNote = "C"
                
            elif change == "ED":
                prob = prob * 0.2
                currentNote = "D"
                
            elif change == "EE":
                prob = prob * 0.1
                currentNote = "E"
                
            elif change == "EF":
                prob = prob * 0.1
                currentNote = "F"
                
            elif change == "EG":
                prob = prob * 0.1
                currentNote = "G"
                
            elif change == "EA":
                prob = prob * 0.2
                currentNote = "A"
                
            elif change == "EB":
                prob = prob * 0.1
                currentNote = "B"
                
            else:
                prob = prob * 0.1
                currentNote = "C2"
                
        elif currentNote == "F":
            change = np.random.choice(transitionName[3],replace=True,p=transitionMatrix[3])
            if change == "FC":
                prob = prob * 0.1
                currentNote = "C"
                
            elif change == "FD":
                prob = prob * 0.2
                currentNote = "D"
                
            elif change == "FE":
                prob = prob * 0.1
                currentNote = "E"
                
            elif change == "FF":
                prob = prob * 0.1
                currentNote = "F"
                
            elif change == "FG":
                prob = prob * 0.1
                currentNote = "G"
                
            elif change == "FA":
                prob = prob * 0.2
                currentNote = "A"
                
            elif change == "FB":
                prob = prob * 0.1
                currentNote = "B"
                
            else:
                prob = prob * 0.1
                currentNote = "C2"
                
        elif currentNote == "G":
            change = np.random.choice(transitionName[4],replace=True,p=transitionMatrix[4])
            if change == "GC":
                prob = prob * 0.1
                currentNote = "C"
                
            elif change == "GD":
                prob = prob * 0.2
                currentNote = "D"
                
            elif change == "GE":
                prob = prob * 0.1
                currentNote = "E"
                
            elif change == "GF":
                prob = prob * 0.1
                currentNote = "F"
                
            elif change == "GG":
                prob = prob * 0.1
                currentNote = "G"
                
            elif change == "GA":
                prob = prob * 0.2
                currentNote = "A"
                
            elif change == "GB":
                prob = prob * 0.1
                currentNote = "B"
                
            else:
                prob = prob * 0.1
                currentNote = "C2"
                
        elif currentNote == "A":
            change = np.random.choice(transitionName[5],replace=True,p=transitionMatrix[5])
            if change == "AC":
                prob = prob * 0.1
                currentNote = "C"
                
            elif change == "AD":
                prob = prob * 0.2
                currentNote = "D"
                
            elif change == "AE":
                prob = prob * 0.1
                currentNote = "E"
                
            elif change == "AF":
                prob = prob * 0.1
                currentNote = "F"
                
            elif change == "AG":
                prob = prob * 0.1
                currentNote = "G"
                
            elif change == "AA":
                prob = prob * 0.2
                currentNote = "A"
                
            elif change == "AB":
                prob = prob * 0.1
                currentNote = "B"
                
            else:
                prob = prob * 0.1
                currentNote = "C2"
                
        elif currentNote == "B":
            change = np.random.choice(transitionName[6],replace=True,p=transitionMatrix[6])
            if change == "BC":
                prob = prob * 0.1
                currentNote = "C"
                
            elif change == "BD":
                prob = prob * 0.2
                currentNote = "D"
                
            elif change == "BE":
                prob = prob * 0.1
                currentNote = "E"
                
            elif change == "BF":
                prob = prob * 0.1
                currentNote = "F"
                
            elif change == "BG":
                prob = prob * 0.1
                currentNote = "G"
                
            elif change == "BA":
                prob = prob * 0.2
                currentNote = "A"
                
            elif change == "BB":
                prob = prob * 0.1
                currentNote = "B"
                
            else:
                prob = prob * 0.1
                currentNote = "C2"
                
                
        elif currentNote == "C2":
            change = np.random.choice(transitionName[7],replace=True,p=transitionMatrix[7])
            if change == "C2C":
                prob = prob * 0.1
                currentNote = "C"
                
            elif change == "C2D":
                prob = prob * 0.2
                currentNote = "D"
                
            elif change == "C2E":
                prob = prob * 0.1
                currentNote = "E"
                
            elif change == "C2F":
                prob = prob * 0.1
                currentNote = "F"
                
            elif change == "C2G":
                prob = prob * 0.1
                currentNote = "G"
                
            elif change == "C2A":
                prob = prob * 0.2
                currentNote = "A"
                
            elif change == "C2B":
                prob = prob * 0.1
                currentNote = "B"
                
            else:
                prob = prob * 0.1
                currentNote = "C2"
                
                
            ran = rm.randint(1,9)
            if ran == 1:
                currentNote = "C"
            elif ran == 2:
                currentNote = "D"
            elif ran == 3:
                currentNote = "E"
            elif ran == 4:
                currentNote = "F"
            elif ran == 5:
                currentNote = "G"
            elif ran == 6:
                currentNote = "A"
            elif ran == 7:
                currentNote = "B"    
            else:
                currentNote = "C2"
            
        print(currentNote)
        result.append(currentNote)
        i += 1
        ran = rm.randint(1,9)
        if ran == 1:
            currentNote = "C"
        elif ran == 2:
            currentNote = "D"
        elif ran == 3:
            currentNote = "E"
        elif ran == 4:
            currentNote = "F"
        elif ran == 5:
            currentNote = "G"
        elif ran == 6:
            currentNote = "A"
        elif ran == 7:
            currentNote = "B"    
        else:
            currentNote = "C2"
    for i in range(len(result)):
        if result[i] == "C":
            final.append(60)
        elif result[i] == "D":
            final.append(62)
        elif result[i] == "E":
            final.append(64)
        elif result[i] == "F":
            final.append(65)
        elif result[i] == "G":
            final.append(67)
        elif result[i] == "A":
            final.append(69)
        elif result[i] == "B":
            final.append(69)
        else:
            final.append(72)
    
    return final
#    for i in range (len(result)):
#        print("r" + result[i])
#t = threading.Thread(target = piece, args = (50,))
#t.start()