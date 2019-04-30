import numpy as np


def viterbi(obs, states, start_p, trans_p, emit_p):
    max_p = np.zeros((len(obs), len(states)))

    path = np.zeros((len(states), len(obs)))

    for i in range(len(states)):
        max_p[0][i] = start_p[i] * emit_p[i][obs[0] - 1]
        path[i][0] = i

    for t in range(1, len(obs)):
        newpath = np.zeros((len(states), len(obs)))
        for y in range(len(states)):
            prob = -1
            for y0 in range(len(states)):
                nprob = max_p[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t] - 1]
                if nprob > prob:
                    prob = nprob
                    state = y0
                    max_p[t][y] = prob
                    for m in range(t):
                        newpath[y][m] = path[state][m]
                    newpath[y][t] = y

        path = newpath

    max_prob = -1
    path_state = 0

    for y in range(len(states)):
        if max_p[len(obs)-1][y] > max_prob:
            max_prob = max_p[len(obs)-1][y]
            path_state = y

    return path[path_state], max_prob

#Read the text file
FILE_NAME = "InputFile7.txt"

p_emission = []
emissions = []

with open(FILE_NAME, "r") as f:
    f.readline()
    p_notswitch = float(f.readline())
    f.readline()
    
    print("Emission probabilities are:","\n")    
    #Read the Emission Probabilities Matrix from file 
    for i in range(3):
         
            p_emission.append([float(p) for p in (f.readline().split(','))])
            print(p_emission[i],"\n")
    
    f.readline()
    emissions = [int(p) for p in f.readline()[1: -1].split(',')]
f.close()


#Create a 3*3 States Transfer Matrix  
trans_matrix = [[0.0]*3 for i in range(3)]
p_switch = (1 - p_notswitch)/2

print("Transition probabilities are:","\n")

for i in range(3):
    for j in range(3):
        if i == j :
            trans_matrix[i][j] = p_notswitch;
        else:
            trans_matrix[i][j] = p_switch;
    print(trans_matrix[i],"\n")

    
print("The alphabet (dice): dice 1, dice 2, dice 3\n")
print("Set of states: {dice 1, dice 2, dice 3}\n")
#Observation States = [1, 2, 3]
state_s = [1, 2, 3]

#Hidden States X=[d1, d2, d3]
hidden_state = ["dice 1", "dice 2", "dice 3"]

#Initial State Probabilities are equal
initial_probability = [1/3, 1/3, 1/3]

transition_probability = np.array(trans_matrix)

emission_probability = np.array(p_emission)

result, max_prob = viterbi(emissions, state_s, initial_probability, transition_probability, emission_probability)

print("The sequence of states which best explains the sequence of rolls: ")
print([hidden_state[int(step)] for step in result])

print("The probability of this sequence: ")
print(max_prob)
