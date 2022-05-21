import numpy as np
import os 
import json
from create_net import topology
from spf import spf

def CLI():
    '''This function gets the desired topology matrix as the input in order to be used in further functions'''

    n = int(input("Please enter the shape of your matrix (n): "))
    
    print("Please enter the matrix in the given format:")
    print("--Enter each row weights with space (eg. 1,2,2,4,2) and then press enter to enter the next row")
    print("--The number of rows would automatically be taken equal to the number of the columns!")
    print("A = ")
    A = []
    i = 0
    while i < n:
        Ai = list(input())
        if (len(Ai) != n):
            print("The number of entered columns is wrong! Please try again.")
        else:
            A.append(Ai)
            i+=1
    return np.array(A)

if __name__=="__main__":
    # creating the matrix
    A = CLI()
    os.makedirs("data", mode=0o777)

    # finding the shortest paths and saving it
    spf_1_n, spf_n_1 = spf(A)
    with open("data/A.json", "w") as f1:
        json.dump(A.tolist(), f1)
    with open("data/spf_1_n.json", "w") as f2:
        json.dump(spf_1_n, f2)
    with open("data/spf_n_1.json", "w") as f3:
        json.dump(spf_n_1, f3)
    
    # creating the network of the given matrix and running the mininet CLI
    topology(A)
