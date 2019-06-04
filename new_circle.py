#Alexis Echano
#Better Circle Lab - Machine Learning and NEURAL NETWORKS
import os, sys, math, random, time

lens = [3, 6, 3, 1, 1, 1]   #layer counts

weights = {0:[[-4.9673,  3.3783, 5.3325],
        [-6.3445,  3.1574, -2.3441],
        [-2.0087, -4.9509, -4.2762],
        [ 6.5002, -1.9621, -5.5667],
        [-6.1747,  3.0646, -5.1309],
        [ 2.7268,  4.1389, -3.8352]],
           1:[[ 6.0741,  -1.1152,  -7.5443,  -1.8647,  -5.3909,  -7.5898],
        [ 6.2047,  -1.2378,  -7.6972,  -1.9337,  -5.3706,  -7.7528],
        [-19.6547,   4.2256,  25.4531,   7.0026,  17.3872,  25.3523]],
           2:[[ 16.0500,  16.1805, -44.1491]],
           3:[[17.3721]], 4:[[0.6807]]}

def adjust_weights(op):  #only fixes the first layer
    index = len(op) - 1
    num_ind = ""
    while index >= 0:
        if op[index] == "=" or op[index] == ">" or op[index] == "<":
            break
        else: num_ind += op[index]
        index-=1
    div_index = math.sqrt(float(num_ind[::-1]))

    new_first = []
    first_layer = weights[0]
    for node in first_layer:
        sub = []
        for val in range(len(node)):
            if val != len(node) - 1:
                curr = node[val]
                sub.append(float(curr/div_index))
            else:
                sub.append(node[val])
        new_first.append(sub)

    weights[0] = new_first  #updates it

def make_it_readable():
    adjusted = []

    for i in weights.keys():
        temp = []
        current = weights[i]
        for sub in current:
            for val in sub:
                temp.append(val)
        adjusted.append(temp)

    return adjusted

def main(): #trains, creates new network based on stuff
    OPERATION = sys.argv[1]
    adjust_weights(OPERATION)
    ws = make_it_readable()
    print("layer counts", lens)
    print("weights", end=" ")
    for w in ws:
        print(w)

#   run main file
main()