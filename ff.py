#   Feeding Forward Lab
#   Alexis Echano Period 7
import os, sys, math

WEIGHTS = {0: [[0.2770149726270103, 0.08599525311594647, 0.1923150548201215],[0.15822995838275988, 0.3125973713795491, 0.7585852143863143]],
          1: [[0.09050538657268319, 0.9295545446844707]], 2: [[0.8159477905497953]]}

#[[0.25518, 0.61789, 0.30937, 0.51403, 0.16494, 0.60455], [0.54951, 0.45905], [0.20541]]
def transfer_function(num, sum_val):   #num is the T#
    if num == 1: return transfunc_one(sum_val)
    elif num == 2: return transfunc_two(sum_val)
    elif num == 3: return transfunc_three(sum_val)
    else: return transfunc_four(sum_val)

def transfunc_one(val): #basic
    return val

def transfunc_two(val): #ramp
    if val >= 0:
        return val
    return 0.0

def transfunc_three(val):   #logistic
    return 1.0/(1.0 + (math.e**(-1.0 * val)))

def transfunc_four(val):    #doubler
    return (2.0 * transfunc_three(val)) - 1.0

def read_file(file_list, leng):   #INPUT LIST OF LINES IN THE THING
    global WEIGHTS
    layer_num = 0   #keep track of which layer

    #leng var is the length of inputs so we can determine values
    weights_per_layer = []
    weights_a_node = []

    #the next value is the len of the previous dict entry!!
    for line in file_list:  #reads line by line, index in value is the transfer node's assignment
        line = line.split()
        if layer_num == 0:
            i = 1
            for num in line:
                num = float(num)
                weights_a_node.append(num)
                if i < leng:
                    i += 1
                else:
                    weights_per_layer.append(weights_a_node)
                    weights_a_node = []
                    i = 1
        else:
            length_new = len(WEIGHTS[layer_num-1])
            x = 1
            for val in line:
                val = float(val)
                weights_a_node.append(val)
                if x < length_new:
                    x += 1
                else:
                    weights_per_layer.append(weights_a_node)
                    weights_a_node = []
                    x = 1

        WEIGHTS[layer_num] = weights_per_layer
        weights_per_layer = []
        layer_num += 1

def dot_product_sum(inputs, weight_list):  #should return a list of lists with same len as weights
    return_lists = []   #sums, index is the weights
    weighted = []

    for node in weight_list:    # node is a list of weights for the next layer
        for x in range(len(node)):
            temp_val = inputs[x] * node[x]
            weighted.append(temp_val)
        return_lists.append(sum(i for i in weighted))
        weighted = []

    return return_lists

def main():
    #args = sys.argv[1:]

    #file_name= args[0]
    #inputs = args[1:]   #input vals
    input_vals = [0.0, 0.0, 1.0] #the float version of these
    transNum = -1

    transNum = int(3)  #creates a num for the transfer function

    #for v in inputs:    #turns all inputs in to numbers
        #input_vals.append(float(v))

    #if os.path.isfile(file_name):
        #dictLine = open(file_name, 'r').read().splitlines()
        #read_file(dictLine, len(input_vals)) #CREATES WEIGHTS DICTIONARY

    layer = 0

    new_inputs = input_vals #put transfer functioned, and added values here for next layer

    while layer < len(WEIGHTS) - 1:
        to_be_trans = dot_product_sum(new_inputs, WEIGHTS[layer])
        new_inputs = []

        for new_node in to_be_trans:
            new_inputs.append(transfer_function(transNum, new_node))

        layer += 1

    #final layer
    final_weights = WEIGHTS[layer][0]
    result = []
    for i in range(len(new_inputs)):
        value = new_inputs[i] * final_weights[i]
        result.append(value)

    for thing in result:
        print(thing, end=" ")
    print()

    print(.5*(0.0-thing)**2)  #error

#   run main file
main()