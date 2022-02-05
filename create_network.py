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
f = open("./qualification_round_2021.in/b.txt")

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

pos=nx.spring_layout(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos, node_size=1500, with_labels=True) #,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
pylab.show()

def status():
    print("INI STATUS: ")
    for car in Cars:
        print("id: {}, street: {}, position: {}/{}, arrived={}".format(car.id, car.street_name, car.position_street,G_data[car.street].tt,car.arrived))
        
    print("\n")
    for s in G_data:
        print("street: {}, arrivals: {}".format(s.name,s.arrivals))
    print("FIN STATUS: ")

def advance_cars():
    for car in Cars:
        if car.arrived:
            # print("car {} end street {}".format(car.id, car.street_name))
            pass
            
        else:
            print("FORWARD: car {} in street {}".format(car.id, car.street_name))
            # advance one position
            car.position_street +=1
            
            
            # arrived end street?
            if car.position_street == car.tt:
                print("car {} arrived end street {}".format(car.id, car.street_name))
                car.arrived=True
                if (car.position_route+1)==len(car.route):
                    print("CAR {} HAS ARRIVED AT DESTINATION!!!".format(car.id))
                else:
                    G_data[car.street].arrivals.append(car.id)
            
        
        
def advance_intersections():        
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
            
            print("INTERSECTION  car {} from {} to {}".format(car.id, s.name, car.street_name))
        
        #change car position
        
def lights(t):
    #intersection 1
    i = t%3
    if i == 2:
        G_data[1].light = "green"
        G_data[2].light = "red"
    else:
        G_data[1].light = "red"
        G_data[2].light = "green"
        
    #intersection 0,2
    G_data[0].light = "green"
    G_data[4].light = "green"

def lights(t):
    for node in G.nodes:
        n_income = len(G.in_edges(node))
        edges = list(G.in_edges(node))
        if n_income == 1:
            street_id = G.get_edge_data(edges[0][0],edges[0][1])['label']
            G_data[street_id].light = "green"
            
        else:
            i = t % n_income
            # print(i)
            for idx,edge in enumerate(edges):
                street_id = G.get_edge_data(edge[0],edge[1])['label']
                if idx==i:
                    G_data[street_id].light = "green"
                
                else:
                    G_data[street_id].light = "red"
                    
                    
                
            
for t in range(12):
    print(t)
    lights(t)
    for i in range(S): print(G_data[i].light )
        
        


for t in range(10):
    
    lights(t)
    advance_cars()
    # status()
    advance_intersections()
    # status()
    # t += 1
    print(t)