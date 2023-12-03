import networkx as nx
import matplotlib.pyplot as plt
import sympy as sy
from Aestrella import astar_path

def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

#create a node class that has two attribute, its name and weight, both are passed in the constructor, it has a constructor and a getter for the weight and another for the name
G = nx.Graph()

#linea A roja
G.add_node("Perrache", linea = ["A"])
G.add_node("Ampère Victor Hugo", linea = ["A"])
G.add_node("Cordeliers", linea = ["A"])
G.add_node("Hôtel De Ville - Louis Pradel", linea = ["A", "C"])
G.add_node("Foch", linea = ["A"])
G.add_node("Masséna", linea = ["A"])
G.add_node("République Villeurbanne", linea = ["A"])
G.add_node("Gratte-Ciel", linea = ["A"])
G.add_node("Flachet", linea = ["A"])
G.add_node("Cusset", linea = ["A"])
G.add_node("Laurent Bonnevay", linea = ["A"])
G.add_node("Vaulx-En-Velin La Soie", linea = ["A"])

#linea B azul
G.add_node("Oullins Gare", linea = ["B"])
G.add_node("Stade De Gerland", linea = ["B"])
G.add_node("Debourg", linea = ["B"])
G.add_node("Place Jean Jaurès", linea = ["B"])
G.add_node("Jean Macé", linea = ["B"])
G.add_node("Saxe Gambetta", linea = ["B"])
G.add_node("Place Guichard Bourse Du Travail", linea = ["B"])
G.add_node("Gare Part-Dieu Vivier Merle", linea = ["B"])
G.add_node("Brotteaux", linea = ["B"])
G.add_node("Charpennes Charles Hernu", linea = ["B", "A"])

#linea C naranja
G.add_node("Cuire", linea = ["C"])
G.add_node("Hénon", linea = ["C"])
G.add_node("Croix-Rousse", linea = ["C"])
G.add_node("Croix-Paquet", linea = ["C"])

#linea D
G.add_node("Gare de Vaise", linea = ["D"])
G.add_node("Valmy", linea = ["D"])
G.add_node("Gorge de Loup", linea = ["D"])
G.add_node("Vieux Lyon Cathedrale St. Jean", linea = ["D"])
G.add_node("Bellecour", linea = ["A","D"])
G.add_node("Guillotière", linea = ["D"])
G.add_node("Saxe Gambetta", linea = ["B", "D"])
G.add_node("Garibaldi", linea = ["D"])
G.add_node("Sans-Souci", linea = ["D"])
G.add_node("Monplalsir - Lumière", linea = ["D"])
G.add_node("Grange Blanche", linea = ["D"])
G.add_node("Laennec", linea = ["D"])
G.add_node("Mermoz Pinel", linea = ["D"])
G.add_node("Parilly", linea = ["D"])
G.add_node("Garre de Venissieux", linea = ["D"])

#linea B


#edge = arista 
G.add_edge("A", "B", weight = 30)
G.add_edge("B", "E", weight = 30)
G.add_edge("E", "F", weight = 30)
G.add_edge("F", "D", weight = 30)
G.add_edge("A", "F", weight = 30)
G.add_edge("C", "D", weight = 30)
G.add_edge("E", "G", weight = 30)
G.add_edge("G", "D", weight = 30)

#create 2-D matrix of zeros with sympy
matrix = sy.zeros(30, 30)

labels = {n: str(n) + ';   ' + str(G.nodes[n]['weight']) for n in G.nodes}
"""G = nx.grid_graph(dim=[3, 3])  # nodes are two-tuples (x,y)
nx.set_edge_attributes(G, {e: e[1][0] * 2 for e in G.edges()}, "cost")"""
path = astar_path(G, "A", "D", heuristic=None, weight="cost")
#length = nx.astar_path_length(G, (0, 0), (2, 2), heuristic=dist, weight="cost")
print("Path: ", path)
#print("Path length: ", length)

""""pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="#f86e00")
edge_labels = nx.get_edge_attributes(G, "cost")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()"""""

import matplotlib.animation as animation
import time

def draw_path_animation(graph, source, target, path, label):
    pos = nx.planar_layout(graph)  # You can use a different layout depending on your graph structure

    def update(frame):
        plt.clf()
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color='lightblue', labels=label)
        
        if frame < len(path) - 1:
            edge = (path[frame], path[frame + 1])
            nx.draw_networkx_edges(graph, pos, edgelist=[edge], edge_color='red', width=2)
            labels = nx.get_edge_attributes(graph, 'weight')
            nx.draw_networkx_edge_labels(graph, pos, labels)

    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, update, frames=len(path), repeat=False, interval=1000)

    plt.show()

draw_path_animation(G, "A", "D", path, labels)


