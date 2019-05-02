import numpy as np

# try InputFile7

#Hidden Markov Model
#Hidden States X=[d1, d2, d3]
#Observation States (label)= [1, 2, 3]
#Transition Probabilities:P(Xt|Xt-1)
#Emission Probabilities:P(Et|Xt)

print("The alphabet is dice1, dice2, dice3\n")
print("The states are {dice1, dice2, dice3}\n")
print("The observation is {1, 2, 3}\n")


def viterbi(obs, states, initial_p, trans_p, emit_p):
    #len(obs): the total time throw dices
    #len(states):the total numbers of label types
    max_p = np.zeros((len(obs), len(states)))

    path = np.zeros((len(states), len(obs)))
   #Initialize 
   #Calculate P(x1|E1) as max_p
    for i in range(len(states)):
        max_p[0][i] = initial_p[i] * emit_p[i][obs[0] - 1]
        path[i][0] = i
   
    for t in range(1, len(obs)):
        newpath = np.zeros((len(states), len(obs)))
        for x in range(len(states)):
            #the max probability of path(x[t-1] then x[t]) at t
            cur_prob = -1
            #From x0 to x[t-1]
            for x0 in range(len(states)):
                #For each possible xt =[d1, d2, d3],calculate the cur_prob from three path and get the max:
                 # 1.x[t-1] = d1 then x[t] = di
                 # 2.x[t-1] = d2 then x[t] = di
                 # 3.x[t-1] = d3 then x[t] = di
                temp_prob = max_p[t-1][x0] * trans_p[x0][x] * emit_p[x][obs[t] - 1]
                if temp_prob > cur_prob:
                    cur_prob = temp_prob
                    state = x0
                    max_p[t][x] = cur_prob
                    #Copy the path from 0 to t-1 to the newpath
                    for m in range(t):
                        newpath[x][m] = path[state][m]
                    #Add x at the the last t to the newpath
                    newpath[x][t] = x

        path = newpath

    max_prob = -1
    #The last state
    path_state = 0 
    
    #When matrix is done, find the max probability in max_p[obs-1],get that state No.
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


#Observation States (label)= [1, 2, 3]
state_s = [1, 2, 3]

#Hidden States X=[d1, d2, d3]
hidden_state = ["dice 1", "dice 2", "dice 3"]

#Initial State Probabilities are equal
initial_probability = [1/3, 1/3, 1/3]

transition_probability = np.array(trans_matrix)

emission_probability = np.array(p_emission)

result, max_prob = viterbi(emissions, state_s, initial_probability, transition_probability, emission_probability)

print("The sequence states which best explains the sequence of rolls: ")
print([hidden_state[int(step)] for step in result],"\n")

print("The probability of this sequence: ", max_prob)

