import networkx as nx
import matplotlib.pyplot as plt
from a_estrella import a_estrella_ruta, a_star

class Ini:
    def __init__(self, inicio, fin, modoObjetivo):
        self.inicio = inicio
        self.fin = fin
        self.modoObjetivo = modoObjetivo

    def ini(self):
        def heuristic(u, v, m = None):
            (x1, y1) = G.nodes[u]['pos']
            (x2, y2) = G.nodes[v]['pos']
            dist  = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            tiempo = dist / 30
            if (m == None):
                return dist
            elif (m == "No transbordos"):
                return tiempo + 1000
            elif (m == "Tiempo"):
                return dist + 5
        
        
        G = nx.Graph()
        #linea A roja
        G.add_node("Perrache", linea = ["A"], pos = (1.339, 3.366))
        G.add_node("Ampère Victor Hugo", linea = ["A"], pos = (1.442, 3.683))
        G.add_node("Cordeliers", linea = ["A"], pos = (1.720, 4.419))
        G.add_node("Hotel De Ville\nLouis Pradel", linea = ["A", "C"], pos = (1.712, 4.737))
        G.add_node("Foch", linea = ["A"], pos = (2.067, 4.849))
        G.add_node("Masséna", linea = ["A"], pos = (2.412, 4.915))
        G.add_node("République Villeurbanne", linea = ["A"], pos = (3.168, 4.989))
        G.add_node("Gratte-Ciel", linea = ["A"], pos = (3.392, 4.859))
        G.add_node("Flachet", linea = ["A"], pos = (3.737, 4.765))
        G.add_node("Cusset", linea = ["A"], pos = (4.120, 4.635))
        G.add_node("Laurent Bonnevay Astroballe", linea = ["A"], pos = (4.500, 4.500))
        G.add_node("Vaulx-En-Velin La Soie", linea = ["A"], pos = (5.043, 4.327))

        #linea B azul
        G.add_node("Oullins Gare", linea = ["B"], pos = (0.901, 0.921))
        G.add_node("Stade De Gerland", linea = ["B"], pos =(1.517, 1.658))
        G.add_node("Debourg", linea = ["B"], pos = (1.638, 2.041))
        G.add_node("Place Jean Jaurès", linea = ["B"], pos = (1.806, 2.657))
        G.add_node("Jean Macé", linea = ["B"], pos = (1.946, 3.095))
        G.add_node("Place Guichard Bourse\nDu Travail", linea = ["B"], pos = (2.179, 4.122))
        G.add_node("Gare Part-Dieu\nVivier Merle", linea = ["B"], pos = (2.524, 4.327))
        G.add_node("Brotteaux", linea = ["B"], pos = (2.608, 4.672))
        G.add_node("Charpennes\nCharles Hernu", linea = ["B", "A"], pos = (2.683, 4.905))

        #linea C naranja
        G.add_node("Cuire", linea = ["C"], pos = (1.600, 6.193))
        G.add_node("Hénon", linea = ["C"], pos = (1.377, 5.558))
        G.add_node("Croix-Rousse", linea = ["C"], pos = (1.545, 5.278))
        G.add_node("Croix-Paquet", linea = ["C"], pos = (1.694, 5.036))

        #linea D verde
        G.add_node("Gare de Vaise", linea = ["D"], pos =(0.490, 5.736))
        G.add_node("Valmy", linea = ["D"], pos = (0.528, 5.325))
        G.add_node("Gorge de Loup", linea = ["D"], pos = (0.528, 4.691))
        G.add_node("Vieux Lyon\nCathedrale St. Jean", linea = ["D"], pos = (1.311, 4.215))
        G.add_node("Bellecour", linea = ["A","D"], pos = (1.591,4.000))
        G.add_node("Guillotière", linea = ["D"], pos = (1.992, 3.851))
        G.add_node("Saxe Gambetta", linea = ["B", "D"], pos = (2.142, 3.748))
        G.add_node("Garibaldi", linea = ["D"], pos =(2.500, 3.500))
        G.add_node("Sans-Souci", linea = ["D"], pos = (2.832, 3.272))
        G.add_node("Monplalsir - Lumière", linea = ["D"], pos = (3.056, 3.077))
        G.add_node("Grange Blanche", linea = ["D"], pos = (3.392, 2.899))
        G.add_node("Laennec", linea = ["D"], pos = (3.588, 2.666))
        G.add_node("Mermoz Pinel", linea = ["D"], pos = (3.6712, 1.901))
        G.add_node("Parilly", linea = ["D"], pos = (3.690,1.313))
        G.add_node("Garre de Venissieux", linea = ["D"], pos = (3.690,0.222))

        #edge = arista 
        G.add_edge("Gare de Vaise", "Valmy", weight = heuristic("Gare de Vaise", "Valmy"))
        G.add_edge("Valmy", "Gorge de Loup", weight = heuristic("Valmy", "Gorge de Loup"))
        G.add_edge("Gorge de Loup", "Vieux Lyon\nCathedrale St. Jean", weight = heuristic("Gorge de Loup", "Vieux Lyon\nCathedrale St. Jean"))
        G.add_edge("Vieux Lyon\nCathedrale St. Jean", "Bellecour", weight = heuristic("Vieux Lyon\nCathedrale St. Jean", "Bellecour"))
        G.add_edge("Bellecour", "Guillotière", weight = heuristic("Bellecour", "Guillotière"))
        G.add_edge("Guillotière", "Saxe Gambetta", weight = heuristic("Guillotière", "Saxe Gambetta"))
        G.add_edge("Saxe Gambetta", "Garibaldi", weight = heuristic("Saxe Gambetta", "Garibaldi"))
        G.add_edge("Garibaldi", "Sans-Souci", weight = heuristic("Garibaldi", "Sans-Souci"))
        G.add_edge("Sans-Souci", "Monplalsir - Lumière", weight = heuristic("Sans-Souci", "Monplalsir - Lumière"))
        G.add_edge("Monplalsir - Lumière", "Grange Blanche", weight = heuristic("Monplalsir - Lumière", "Grange Blanche"))
        G.add_edge("Grange Blanche", "Laennec", weight = heuristic("Grange Blanche", "Laennec"))
        G.add_edge("Laennec", "Mermoz Pinel", weight = heuristic("Laennec", "Mermoz Pinel"))
        G.add_edge("Mermoz Pinel", "Parilly", weight = heuristic("Mermoz Pinel", "Parilly"))
        G.add_edge("Parilly", "Garre de Venissieux", weight = heuristic("Parilly", "Garre de Venissieux"))
        G.add_edge("Cuire", "Hénon", weight = heuristic("Cuire", "Hénon"))
        G.add_edge("Hénon", "Croix-Rousse", weight = heuristic("Hénon", "Croix-Rousse"))
        G.add_edge("Croix-Rousse", "Croix-Paquet", weight = heuristic("Croix-Rousse", "Croix-Paquet"))
        G.add_edge("Croix-Paquet", "Hotel De Ville\nLouis Pradel", weight = heuristic("Croix-Paquet", "Hotel De Ville\nLouis Pradel"))
        G.add_edge("Charpennes\nCharles Hernu", "Brotteaux", weight = heuristic("Charpennes\nCharles Hernu", "Brotteaux"))
        G.add_edge("Brotteaux", "Gare Part-Dieu\nVivier Merle", weight = heuristic("Brotteaux", "Gare Part-Dieu\nVivier Merle"))
        G.add_edge("Gare Part-Dieu\nVivier Merle", "Place Guichard Bourse\nDu Travail", weight = heuristic("Gare Part-Dieu\nVivier Merle", "Place Guichard Bourse\nDu Travail"))
        G.add_edge("Place Guichard Bourse\nDu Travail", "Saxe Gambetta", weight = heuristic("Place Guichard Bourse\nDu Travail", "Saxe Gambetta"))
        G.add_edge("Saxe Gambetta", "Jean Macé", weight = heuristic("Saxe Gambetta", "Jean Macé"))
        G.add_edge("Jean Macé", "Place Jean Jaurès", weight = heuristic("Jean Macé", "Place Jean Jaurès"))
        G.add_edge("Place Jean Jaurès", "Debourg", weight = heuristic("Place Jean Jaurès", "Debourg"))
        G.add_edge("Debourg", "Stade De Gerland", weight = heuristic("Debourg", "Stade De Gerland"))
        G.add_edge("Stade De Gerland", "Oullins Gare", weight = heuristic("Stade De Gerland", "Oullins Gare"))
        G.add_edge("Perrache", "Ampère Victor Hugo", weight = heuristic("Perrache", "Ampère Victor Hugo"))
        G.add_edge("Ampère Victor Hugo", "Bellecour", weight = heuristic("Ampère Victor Hugo", "Bellecour"))
        G.add_edge("Bellecour", "Cordeliers", weight = 30)
        G.add_edge("Cordeliers", "Hotel De Ville\nLouis Pradel", weight = heuristic("Cordeliers", "Hotel De Ville\nLouis Pradel"))
        G.add_edge("Hotel De Ville\nLouis Pradel", "Foch", weight = heuristic("Hotel De Ville\nLouis Pradel", "Foch"))
        G.add_edge("Foch", "Masséna", weight = heuristic("Foch", "Masséna"))
        G.add_edge("Masséna", "Charpennes\nCharles Hernu", weight = heuristic("Masséna", "Charpennes\nCharles Hernu"))
        G.add_edge("Charpennes\nCharles Hernu", "République Villeurbanne", weight = heuristic("Charpennes\nCharles Hernu", "République Villeurbanne"))
        G.add_edge("République Villeurbanne", "Gratte-Ciel", weight = heuristic("République Villeurbanne", "Gratte-Ciel"))
        G.add_edge("Gratte-Ciel", "Flachet", weight = heuristic("Gratte-Ciel", "Flachet"))
        G.add_edge("Flachet", "Cusset", weight = heuristic("Flachet", "Cusset"))
        G.add_edge("Cusset", "Laurent Bonnevay Astroballe", weight = heuristic("Cusset", "Laurent Bonnevay Astroballe"))
        G.add_edge("Laurent Bonnevay Astroballe", "Vaulx-En-Velin La Soie", weight = heuristic("Laurent Bonnevay Astroballe", "Vaulx-En-Velin La Soie"))


        #labels = {n: str(n) + ';   ' + str(G.nodes[n]['weight']) for n in G.nodes}
        """G = nx.grid_graph(dim=[3, 3])  # nodes are two-tuples (x,y)
        nx.set_edge_attributes(G, {e: e[1][0] * 2 for e in G.edges()}, "cost")"""
        #path = a_estrella_ruta(G, "Gare de Vaise", "Brotteaux", heuristic, weight="weight", modoObjetivo = "Tiempo")
        path = a_star(G, self.inicio, self.fin, heuristic, modoObjetivo = self.modoObjetivo)
        #length = nx.astar_path_length(G, (0, 0), (2, 2), heuristic=dist, weight="cost")
        print("Path: ", path)
        #print("Path length: ", length)

        pos = nx.get_node_attributes(G, 'pos')
        plt.figure(figsize=(12, 9))
        nx.draw(G, pos, with_labels=True, node_color="#f86e00", font_size = 7)
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
        #edge_labels = nx.get_edge_attributes(G, "cost")
        #nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.xlim(0, 6)
        plt.ylim(0, 7)
        plt.show()

        import matplotlib.animation as animation
        import time

        def draw_path_animation(graph, source, target, path, label = None):
            pos = nx.get_node_attributes(graph, 'pos')  # You can use a different layout depending on your graph structure

            def update(frame):
                plt.clf()
                plt.figure(figsize=(12, 9))
                nx.draw(graph, pos, with_labels=True, node_color='lightblue', font_size=7)
                plt.xlim(0, 6)
                plt.ylim(0, 7)
                
                if frame < len(path) - 1:
                    edge = (path[frame], path[frame + 1])
                    nx.draw_networkx_edges(graph, pos, edgelist=[edge], edge_color='red', width=2)
                    labels = nx.get_edge_attributes(graph, 'weight')
                    nx.draw_networkx_edge_labels(graph, pos, labels)

            fig, ax = plt.subplots()
            ani = animation.FuncAnimation(fig, update, frames=len(path), repeat=False, interval=1000)

            plt.show()

        """draw_path_animation(G, "Gare de Vaise", "Brotteaux", path, None)"""


