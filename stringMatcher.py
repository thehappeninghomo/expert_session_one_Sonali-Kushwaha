# Importing required module
import numpy as np

# Creating the function below to measure the minimum number of edits required to convert one string into other
def levenshteinDistanceRatio(s, t, ratio_calc = True):

    # Initializing a matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Filling it with the indices of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Looping over it to compute the cost of single-character edits    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                # same charcter will cost 0
                cost = 0 
            else:                
                # Handling the results according to Python Levenshtein package
                if ratio_calc == True: cost = 2
                else: cost = 1
            
            # Finding least of single-character editing cost(deletion,insertion,substitution)
            distance[row][col] = min(distance[row-1][col] + 1,distance[row][col-1] + 1,distance[row-1][col-1] + cost)      
    
    # Lastly, Computing the Levenshtein Distance Ratio
    Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
    return Ratio