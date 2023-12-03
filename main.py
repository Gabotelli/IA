import networkx as nx
import matplotlib.pyplot as plt
from Aestrella import astar_path

def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

#create a node class that has two attribute, its name and weight, both are passed in the constructor, it has a constructor and a getter for the weight and another for the name
G = nx.Graph()
G.add_node("A", weight=1)
G.add_node("B", weight=5)
G.add_node("C", weight=1)
G.add_node("D", weight=3)
G.add_node("E", weight=1)
G.add_node("F", weight=0)
G.add_node("G", weight=2)
G.add_edge("A", "C", weight=1)
G.add_edge("A", "B", weight=10)
G.add_edge("B", "E", weight=5)
G.add_edge("E", "F", weight=1)
G.add_edge("F", "D", weight=3)
G.add_edge("A", "F", weight=2)
G.add_edge("C", "D", weight=0)
G.add_edge("E", "G", weight=4)
G.add_edge("G", "D", weight=5)

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


