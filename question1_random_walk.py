import csv #importing csv module
import random #importing random module
import networkx as nx #importing networkx as nx
import matplotlib.pyplot as plt #importing matplotlib.pyplot as plt

#Question 1

G = nx.DiGraph() #initialising a directed graph

#reading a csv file and creating a directed graph
with open("impressionNetwork.csv", 'r') as file: #path of the file on my laptop
    read = csv.reader(file) #reading the csv file
    next(read) #skipping the first row
    for row in read: #iterating through the rows
        for i in range(1, len(row)): #iterating through the column
            if row[i] != 'None': #skipping the cells which have None, these cells indicate no edge in the graph
                G.add_edge(row[0], row[i]) #adding edge to the graph

#to plot the graph
nx.draw(G, with_labels = True)
plt.show()

def randomWalk(G): #defining a function randomwalk to implement page rank
    nodes = list(G.nodes()) #creating a list of nodes
    rw_coins = {node:0 for node in nodes} #initialising a dictionary to store the number of coins corresponding to each node
    n = random.choice(nodes) #choosing a node at random
    rw_coins[n] += 1 #incrementing the value of the randomly chosen node by 1
    out = list(G.out_edges(n)) #creating a list of all the edges emerging from that node
    count = 0 #initialising a variable count to keep a track of number of iterations
    while(count != 1000000) : #while loop, iterating for a million times to ensure that each node gets traversed
        if(len(out) == 0): #if we reach a node from which no edge emerges, we choose a random node from the graph
            focus = random.choice(nodes) 
        else:
            t = random.uniform(0,1) #this is done for teleportation
            if t < 0.15: #if the random number between zero and one is less than 0.15, we choose a node at random from the graph
                n1 = random.choice(nodes) #choosing from the list of nodes
                focus = n1 
            else:
                n1 = random.choice(out) #choosing an edge from the list of edges
                focus = n1[1] #out is a list of tuples which stores edges in the form of tuples, 
                #the second element of the tuple would be the node to which our original node points
        rw_coins[focus] += 1 #incrementing the number of coins
        out = list(G.out_edges(focus)) #updating the out list
        count += 1 #updating the number of iterations
    return rw_coins #returning

RW_points = randomWalk(G) #function call

# Sort the nodes based on their RW points
sorted_RW_points = sorted(RW_points.items(), key=lambda x: x[1], reverse=True) #this is done to sort the dictionary based on its values
#these values are the number of coins with each node and sorting the dictionary in this manner gives pagerank
print(sorted_RW_points) #pagerank
