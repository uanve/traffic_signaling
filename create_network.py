import os
import numpy as np

os.chdir('C:/Users/joanv/OneDrive/Escritorio/code/traffic_signaling')


class Street:
    def __init__(self, id, name, Origin, Destination, tt ):

        self.id = id 
        self.name = name 
        self.Origin = int(Origin)
        self.Destination = int(Destination)
        self.tt = int(tt)
        self.arrivals = []
        self.light = "red"
        
    
            
class Car:
    def __init__(self, id, list_streets):
        # car
        self.id = id
        
        # route 
        self.route = list_streets
        self.position_route = 0
        
        # street
        self.street = list_streets[0]
        self.street_name = id_to_street[self.street]
        self.tt = G_data[self.street].tt
        self.position_street = self.tt
        self.arrived = True
        
        # add initial position
        G_data[self.street].arrivals.append(self.id)
        
        
# Get data from file
f = open("./qualification_round_2021.in/c.txt")

#first file line
# D: simulation duration
# I: Nº intersections
# S: Nº streets
# V: Nº vehicles
# F: bonus point car reach destination
D, I, S, V, F = [int(i) for i in next(f)[:-1].split(" ")]

# street name    +    Origin - Destination Edges
street_to_id = {}
G_data = []

for i in range(S):
    O_node, D_node, street_name, tt = next(f)[:-1].split(" ")
    street_to_id[street_name] = i
    # G_data.append((O_node, D_node, street_name, tt))
    new_street = Street(i, street_name, O_node, D_node, tt)
    
    G_data.append(new_street)
del O_node, D_node, street_name, tt
id_to_street = {v: k for k, v in street_to_id.items()}
    
# Car plan
Cars = []
for i in range(10,10+V):
    next_line = next(f)[:-1].split(" ")
    n_streets, streets = next_line[0], next_line[1:]
    # plan.append((n_streets,streets))
    list_streets = [street_to_id[s] for s in streets]
    new_car = Car(i, list_streets)
    
    Cars.append(new_car)
# del next_line, n_streets, streets
f.close()
    

# Draw network
import networkx as nx
import matplotlib.pyplot as plt
import pylab

G = nx.DiGraph()

for s in G_data:
    G.add_edge(s.Origin, s.Destination, weight=s.tt, label = s.id)    

edge_labels=dict([((u,v,),d['label']) for u,v,d in G.edges(data=True)])
# red_edges = [('C','D'),('D','A')]
# edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

# pos=nx.spring_layout(G)
# nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
# nx.draw(G,pos, node_size=1500, with_labels=True) #,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
# pylab.show()

def status():
    print("INI STATUS: ")
    for car in Cars:
        print("id: {}, street: {}, position: {}/{}, arrived={}".format(car.id, car.street_name, car.position_street,G_data[car.street].tt,car.arrived))
        
    print("\n")
    for s in G_data:
        print("street: {}, arrivals: {}".format(s.name,s.arrivals))
    print("FIN STATUS: ")
    
arrived_car = []

def advance_cars(t):
    for car in Cars:
        if car.arrived:
            # print("car {} end street {}".format(car.id, car.street_name))
            pass
            
        else:
            #go forward
            # print("FORWARD: car {} in street {}".format(car.id, car.street_name))
            # advance one position
            car.position_street +=1
            
            
            # arrived end street?
            if car.position_street == car.tt:
                #has arrived
                # print("car {} arrived end street {}".format(car.id, car.street_name))
                car.arrived=True
                if (car.position_route+1)==len(car.route):
                    #has arrived destination
                    # print("CAR {} HAS ARRIVED AT DESTINATION!!!".format(car.id))
                    arrived_car.append((car.id, t))
                else:
                    G_data[car.street].arrivals.append(car.id)
            
        
def advance_intersections(t):        
    for s in G_data:
        if s.light == "green" and len(s.arrivals)>0:
            #first car in arrivals in
            car_id = s.arrivals[0]
            car = Cars[car_id-10]
            car.arrived = False
            s.arrivals = s.arrivals[1:]
            
            car.position_route += 1
            car.street = car.route[car.position_route]
            car.street_name = id_to_street[car.street]
            car.position_street = 0
            car.tt = G_data[car.street].tt
            #enters intersection
            # print("INTERSECTION  car {} from {} to {}".format(car.id, s.name, car.street_name))
        
###### LIGHT PROGRAM #######
node_with_in_edges = []

edge_to_street = {}
for edge in G.edges:
    edge_to_street[edge] = G.get_edge_data(edge[0],edge[1])['label']
    

for node in G.nodes:
    n_income = len(G.in_edges(node))
    edges = list(G.in_edges(node))
    if n_income == 1:
        street_id = G.get_edge_data(edges[0][0],edges[0][1])['label']
        G_data[street_id].light = "green"
        
    else:
        node_with_in_edges.append((node,len(edges),edges))
        
       

def lights(t):
    for i,node in enumerate(node_with_in_edges):
        i = t%node[1]
        for idx,edge in enumerate(node[2]): 
            street_id = edge_to_street[edge]
            if idx==i:
                G_data[street_id].light = "green"
            
            else:
                G_data[street_id].light = "red"
                    
###### LIGHT PROGRAM #######

###### NEW LIGHT PROGRAM #######
print("Nª intersections: ",I)
s_intersection = [s.Destination for s in G_data]
# size_intersection = [(i, s_intersection.count(i)) for i in range(I)]
# size_intersection.sort(key=lambda x: x[1], reverse=True)
size_intersection = [s_intersection.count(i) for i in range(I)]
intersection_to_streets = {}
for intersection in range(I):
    intersection_to_streets[intersection]=[i for i,val in enumerate(s_intersection) if val==intersection]


size_inter_ = [c for c in size_intersection]
[(i,size_inter_.count(i)) for i in set(size_inter_)]

for i in range(I):
    size = size_intersection[i]
    if size == 1:
        street_id = intersection_to_streets[i][0]
        G_data[street_id].light = "green"
        
    else:
        pass
    
def lights(t):
    for i in range(I):
        size = size_intersection[i]
        if size>=2:
            which_is_green( intersection_to_streets[i])
            
            # street_0, street_1 = intersection_to_streets[i]
            
            # d_0, d_1 = len(G_data[street_0].arrivals), len(G_data[street_1].arrivals)
            
            
            # if d_0+d_1 == 0:
            #     G_data[street_0].light = "red"
            #     G_data[street_1].light = "red"
            # elif d_0==0 and d_1>0:
            #     G_data[street_0].light = "red"
            #     G_data[street_1].light = "green"
                
            # elif d_0>0 and d_1==0:
            #     G_data[street_0].light = "green"
            #     G_data[street_1].light = "red"
            
            # else:
            #     w_0 = d_0/(d_0+d_1)
            #     # w_1 = d_1/(d_0+d_1)
            #     if np.random.rand() < w_0:
            #         G_data[street_0].light = "green"
            #         G_data[street_1].light = "red"
            #     else:
            #         G_data[street_0].light = "red"
            #         G_data[street_1].light = "green"

import random                    
def which_is_green(street_ids):
    len_arrivals = [len(G_data[s].arrivals) for s in street_ids]
    total = sum(len_arrivals)
    if total==0:
        return
    else:
        for s in street_ids: G_data[s].light = "red"
        weights = [len_i/total for len_i in len_arrivals]
        s_chosen = random.choices(street_ids, weights)[0]
        
        G_data[s_chosen].light = "green"
        
        return s_chosen

###### NEW LIGHT PROGRAM #######

    
len_queue_time = np.zeros((D,S))   



import time        
from tqdm import tqdm        
print("Start Loop:")
# for t in range(10):
for t in tqdm(range(D)):
    lights(t)
    advance_cars(t)
    advance_intersections(t)
    
    for i,s in enumerate(G_data):
        len_queue_time[(t,i)] = len(s.arrivals)
    # print(t)

score = 1000 * len(arrived_car) + sum([D-c[1] for c in arrived_car])
print("{}/{} veh. arrived with a total score of {}".format(len(arrived_car), V,score))


plt.hist([e[1] for e in arrived_car],bins=100)


plt.plot(np.mean(len_queue_time,axis=1))
plt.plot(np.mean(len_queue_time,axis=0))

node_queue = [(i,e) for i,e in enumerate(np.mean(len_queue_time,axis=0))]
node_queue.sort(key=lambda x: x[1], reverse=True)

plt.plot(len_queue_time[:,8229])



#Statistics
def get_streets_intersection(street_id):
    node = G_data[street_id].Destination
    return [edge_to_street[s] for s in G.in_edges(node)]


plt.plot(len_queue_time[:2000,7252])
for s in get_streets_intersection(7252):
    plt.plot(len_queue_time[:50,s],label=s)
    plt.legend()
    
    

        
        
        
        
        
                
                    
                
                
                
            
            
        
    

    

    