#   BP Lab
#   Alexis Echano Period 7
import os, sys, math, random, time

FILEINFO = []

OUTPUTS = []
INPUTCT = -1
lens = [INPUTCT+1, 2, 1, 1]    #only first index changes, 3 is placeholder

ALPHA = 0.1  #adjust every so often, based in improvements or error value

def feed_forward(FF, W):         #DONE
    layer = 0
    FEEDFORWARD = FF
    WEIGHTS = W

    new_inputs = FEEDFORWARD[0]

    while layer < len(WEIGHTS) - 1:

        #print(WEIGHTS[layer])
        len_of_next = lens[layer+1]
        if (len_of_next != 1):
            to_be_trans=[]
            b = WEIGHTS[layer][:len(WEIGHTS[layer]) // len_of_next]
            c = WEIGHTS[layer][len(WEIGHTS[layer]) // len_of_next:]

            val = dot_product_sum(new_inputs, b)
            val2 = dot_product_sum(new_inputs, c)
            to_be_trans.append(val)
            to_be_trans.append(val2)

        else:
            to_be_trans = [dot_product_sum(new_inputs, WEIGHTS[layer])]

        new_inputs = []

        for new_node in to_be_trans:
            new_inputs.append(transfer_function(new_node))

        FEEDFORWARD[layer+1] = new_inputs
        layer += 1

    # final layer

    final_weights = WEIGHTS[layer]

    #for i in range(len(new_inputs)):
    result = new_inputs[0] * final_weights[0]
    FEEDFORWARD[layer+1] = [result]
    return result, FEEDFORWARD, WEIGHTS

def dot_product_sum(inputs, weight_list):  #WORKING should return a list of lists with same len as weights
    sum = 0

    for x in range(len(inputs)):
        val = inputs[x] * weight_list[x]
        sum += val

    return sum

def back_propag(weights, inputs, training):
    BP = [[], [], [], []]
    gradients = [[], [], [], []]

    BP[len(inputs) - 1] = [training - inputs[len(inputs) - 1][0]]   #first layer

    v = len(inputs) - 2

    while v > 0:

        for z in range(len(weights[v])):
            gradients[v].append(BP[v + 1][0] * inputs[v][z])    #first gradient

        for d in range(len(inputs[v])):
            BP[v].append(weights[v][d] * BP[v + 1][0] * inputs[v][d] * (1.0 - inputs[v][d]))  # next layer node

        v -= 1

    for val in inputs[0]:
        BP[0].append(val)

    #the final ones
    for a in range(lens[1]):
        for x in range(len(inputs[0])):
            gradients[0].append(BP[1][a] * inputs[0][x])
    return BP, update_weights(weights, gradients)

def transfer_function(sum_val):   #WORKING logistic function
    return 1.0 / (1.0 + (math.e ** (-1.0 * sum_val)))

def read_and_initalize(file_list):   #INPUT LIST OF LINES IN THE THING, init the input count        DONE
    global OUTPUTS, INPUTCT, lens, FILEINFO

    for linez in file_list:
        stuff = []
        line = linez.split()
        x = 0

        while not line[x] == '=>':
            stuff.append(int(line[x]))
            x += 1

        stuff.append(1)

        x += 1
        INPUTCT = x

        OUTPUT = float(line[x])
        OUTPUTS.append(OUTPUT)
        FILEINFO.append(stuff)

        lens[0] = INPUTCT

def update_weights(WE, GRADIENTS):
    WEIGHTS = WE
    w = 0
    while w < len(WEIGHTS):
        x = 0
        while x < len(WEIGHTS[w]):
            WEIGHTS[w][x] += (GRADIENTS[w][x] * ALPHA)
            x += 1
        w += 1
    return WEIGHTS

def calc_final_error(error_list, FEEDFORWARD, ind):    #mean squared error oF OUTPUT
    newErr = error_list[1:]

    temp = 0.5*((OUTPUTS[ind] - FEEDFORWARD[len(FEEDFORWARD)-1][0])**2)
    newErr.append(temp)

    return sum(e for e in newErr), newErr

def check_effectiveness(cost):  #just ensures that i get a 100
    if cost > 0.009:
        return False
    else:
        return True

def initialize_nodes(inputcount, WE): #WORKING 3 layers worth of weights, inputcount DOES NOT INCLUDE BIAS
    global lens
    WEIGHTS = WE
    x = 0

    while x < (lens[0] - 1):
        temp = []
        for r in range(lens[x + 1]):
            for v in range(lens[x]):
                placeholder = random.uniform(-2.0, 2.0)   #decimal between 0 and 1
                temp.append(placeholder)
        WEIGHTS.append(temp)
        x += 1
    return WEIGHTS

def main(): #trains, creates new network based on stuff
    file_name = sys.argv[1]

    if os.path.isfile(file_name):
        dictLine = open(file_name, 'r').read().splitlines()

        read_and_initalize(dictLine)

        weights = initialize_nodes(INPUTCT, [])

        ERRORS = [10] * len(FILEINFO)
        done = False
        minError = 1000

        lens[0] = len(FILEINFO[0])
        start = time.time()
        sum_rors = 0

        for i in range(200000):
            if not done and (time.time() - start) < 27:
                for t in range(len(FILEINFO)):
                    if i >= 60000 and sum_rors > 0.1:#not check_effectiveness(sum_rors):
                        weights = initialize_nodes(INPUTCT, [])

                    trial = FILEINFO[t]

                    FEEDFOR = [trial, [], [], []]  # index 0 is the inputs * weight of layer 0

                    outFF, FEEDFOR, weights = feed_forward(FEEDFOR, weights)

                    BACKP, weights = back_propag(weights, FEEDFOR, OUTPUTS[t])

                    outFF, FEEDFOR, weights= feed_forward(FEEDFOR, weights)

                    sum_rors, ERRORS = calc_final_error(ERRORS, FEEDFOR, t)

                    if sum_rors < minError:
                        minError = sum_rors

                    if check_effectiveness(sum_rors):
                        done = True
                        break

            else:
                break

        print("layer counts", lens)
        print("weights", end = " ")
        for w in weights:
            print(w)

        print()
        print("LIST:",ERRORS)
        print("SUM:", sum_rors)
        print()
        print("MIN ERROR!", minError)
        print()

#   run main file
main()