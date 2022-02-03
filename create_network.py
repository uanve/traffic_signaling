import os

os.chdir('C:/Users/joanv/OneDrive/Escritorio/code/traffic_signaling')



# Get data from file
f = open("./qualification_round_2021.in/a.txt")

#first file line
# D: simulation duration
# I: Nº intersections
# S: Nº streets
# V: Nº vehicles
# F: bonus point car reach destination
D, I, S, V, F = [int(i) for i in next(f)[:-1].split(" ")]

# street name    +    Origin - Destination Edges
street_to_OD = {}
G_data = []

for i in range(S):
    O_node, D_node, street_name, tt = next(f)[:-1].split(" ")
    street_to_OD[street_name] = (O_node,D_node)
    G_data.append((O_node, D_node, street_name, tt))
    
# Car plan
plan = []
for i in range(V):
    next_line = next(f)[:-1].split(" ")
    n_streets, streets = next_line[0], next_line[1:]
    plan.append((n_streets,streets))
    
f.close()
    

# Draw network
import networkx as nx
import matplotlib.pyplot as plt
import pylab

G = nx.DiGraph()

for g in G_data:
    G.add_edge(g[0],g[1], weight=int(g[3]), label = g[2])    

edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
# red_edges = [('C','D'),('D','A')]
# edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

pos=nx.spring_layout(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos, node_size=1500, with_labels=True) #,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
pylab.show()

class Street:
    def __init__(self, id, name, Origin, Destination, tt, ):
    self.name = name
    self.age = age




