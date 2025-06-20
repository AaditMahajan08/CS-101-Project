import csv #importing csv module
import networkx as nx #importing networkx as nx

#Question 3 In a social network represented as a directed graph, each node represents a person, and directed
#edges represent influence or opinion sharing from one person to another. Your task is to identify
#individuals who have the most significant influence in propagating opinions within the network

G = nx.DiGraph() #initialising a directed graph

#reading a csv file and creating a directed graph
with open("impressionNetwork.csv", 'r') as file: #path of the file on my laptop
    read = csv.reader(file) #reading the csv file
    next(read) #skipping the first row
    for row in read: #iterating through the rows
        for i in range(1, len(row)): #iterating through the column
            if row[i] != 'None': #skipping the cells which have None, these cells indicate no edge in the graph
                G.add_edge(row[0], row[i]) #adding edge to the graph

influence_ratios = {node: len(G.in_edges(node)) / max(1, len(G.out_edges(node))) for node in G.nodes()} 
'''influence ratios is a dictionary which stores the 
entry nos as key and the influence ratio for each node as its value
len(G.in_edges(node)): This calculates the number of incoming edges for the current node
len(G.out_edges(node)): This calculates the number of outgoing edges for the current node.
max(1, len(G.out_edges(node))): This part ensures that we don't divide by zero in case the node has no outgoing edges. 
 It takes the maximum of 1 and the number of outgoing edges to avoid division by zero.'''

sorted_influential_people = sorted(influence_ratios.items(), key=lambda x: x[1], reverse=True) 
'''sorted_influential_people = sorted(influence_ratios.items(),
key=lambda x: x[1], reverse=True)}: This line ranks the influential people based on their influence ratio calculated in the previous step.
It sorts the dictionary influence_ratios based on the values (the influence ratios) in descending order.'''

print("Ranked influential people:")
for rank, (person, ratio) in enumerate(sorted_influential_people, start=1):
    print(f"Rank {rank}: {person} - Influence Ratio: {ratio}")
