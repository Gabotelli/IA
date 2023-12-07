import datetime as dt
import math as m
import time as t

import matplotlib.pyplot as plt
import networkx as nx

from a_estrella import a_star


class Ini:
    def __init__(self, inicio, fin, modoObjetivo, tiempoTransbordo = 5):
        self.inicio = inicio
        self.fin = fin
        self.modoObjetivo = modoObjetivo
        self.tiempoTransbordo = tiempoTransbordo

    def ini(self):
        def heuristic(nodoHijo, nodoObjetivo, nodoPadre, lineaActual, nTransbordos):
            (x1, y1) = G.nodes[nodoObjetivo]['pos']
            (x2, y2) = G.nodes[nodoHijo]['pos']
            dist  = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            time = dt.datetime(2003, 6, 18, 9, 36, 0)
            time_change = dt.timedelta(minutes = 40)
            time = time + time_change
            #Calculamos el tiempo con el factor 0.339 unidades/min
            tiempo = dist / 0.339
            tiempo += 1000 * nTransbordos
            lineaHijo = G.nodes[nodoHijo]['linea']
            if lineaActual not in lineaHijo:
                if self.modoObjetivo == "No transbordos" and lineaActual is not None:
                    tiempo = tiempo + 1000
                    nTransbordos += 1

                else :
                    tiempo + self.tiempoTransbordo
                
                """horario = None
                frecuencia = None
                match set(G.nodes[nodoHijo]['linea']) & set(G.nodes[nodoPadre]['linea']) :
                    case "A":
                        horario = self.A
                        frecuencia = 3
                    case "B":
                        horario = self.B
                        frecuencia = 2
                    case "C":
                        horario = self.C
                        frecuencia = 5
                    case "D":
                        horario = self.D
                        frecuencia = 2
                linea = horario[0]
                pos = linea.index(nodoPadre)
                desfase = 0
                if pos != 0 and (pos == len(linea)-1 or horario[pos-1] == nodoHijo):
                    desfase = horario[2][pos-1]
                elif pos == 0 or horario[pos+1] == nodoHijo:
                    desfase = horario[1][pos+1]
                desfase %= frecuencia
                espera = m.ceil((hora-desfase)/frecuencia)*frecuencia+desfase-hora"""

            return [tiempo, nTransbordos]
            #Evaluar linea actual para ver si hay que esperar en estacion
            #Evaluar si hay que cambiar de linea
            #Evaluar el modo
            #nodoHijo, nodoPadre, nodoObjetivo, lineaActual, modoObjetivo
        self.sentido = False
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

        self.A = [["Perrache","Ampère Victor Hugo","Bellecour","Cordeliers","Hotel De Ville\nLouis Pradel","Foch","Masséna","Charpennes\nCharles Hernu","République Villeurbanne","Gratte-Ciel",
                   "Flachet","Cusset","Laurent Bonnevay Astroballe","Vaulx-En-Velin La Soie"],[0,1,2,4,5,7,8,10,11,13,14,16,17,18],[18,17,16,14,13,11,10,8,7,5,4,2,1,0]]

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

        self.B=[["Oullins Gare","Stade De Gerland","Debourg","Place Jean Jaurès","Jean Macé","Saxe Gambetta","Place Guichard Bourse\nDu Travail",
                 "Gare Part-Dieu\nVivier Merle","Brotteaux","Charpennes\nCharles Hernu"],[0,2,3,6,8,10,12,14,15,16],[16,14,13,10,8,6,4,2,1,0]]
        
        #linea C naranja
        G.add_node("Cuire", linea = ["C"], pos = (1.600, 6.193))
        G.add_node("Hénon", linea = ["C"], pos = (1.377, 5.558))
        G.add_node("Croix-Rousse", linea = ["C"], pos = (1.545, 5.278))
        G.add_node("Croix-Paquet", linea = ["C"], pos = (1.694, 5.036))

        self.C=[["Cuire","Hénon","Croix-Rousse","Croix-Paquet","Hotel De Ville\nLouis Pradel"],[0,2,5,7,9],[9,7,4,2,0]]

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

        self.D=[["Gare de Vaise","Valmy","Gorge de Loup","Vieux Lyon\nCathedrale St. Jean","Bellecour","Guillotière","Saxe Gambetta","Garibaldi","Sans-Souci","Monplalsir - Lumière",
                 "Grange Blanche","Laennec","Mermoz Pinel","Parilly","Garre de Venissieux"],[0,2,4,6,8,9,11,12,14,15,17,18,20,22,24],[24,22,20,18,16,15,13,12,10,9,7,6,4,2,0]]

        #edge = arista
        G.add_edge("Gare de Vaise", "Valmy", weight = 2) #pon el peso en weight en el resto
        G.add_edge("Valmy", "Gorge de Loup", weight = 2)
        G.add_edge("Gorge de Loup", "Vieux Lyon\nCathedrale St. Jean", weight = 2)
        G.add_edge("Vieux Lyon\nCathedrale St. Jean", "Bellecour", weight = 2)
        G.add_edge("Bellecour", "Guillotière", weight = 1)
        G.add_edge("Guillotière", "Saxe Gambetta", weight = 2)
        G.add_edge("Saxe Gambetta", "Garibaldi", weight = 1)
        G.add_edge("Garibaldi", "Sans-Souci", weight = 2)
        G.add_edge("Sans-Souci", "Monplalsir - Lumière", weight = 1)
        G.add_edge("Monplalsir - Lumière", "Grange Blanche", weight = 2)
        G.add_edge("Grange Blanche", "Laennec", weight = 1)
        G.add_edge("Laennec", "Mermoz Pinel", weight = 2)
        G.add_edge("Mermoz Pinel", "Parilly", weight = 2)
        G.add_edge("Parilly", "Garre de Venissieux", weight = 2)
        G.add_edge("Cuire", "Hénon", weight = 2)
        G.add_edge("Hénon", "Croix-Rousse", weight = 3)
        G.add_edge("Croix-Rousse", "Croix-Paquet", weight = 2)
        G.add_edge("Croix-Paquet", "Hotel De Ville\nLouis Pradel", weight = 2)
        G.add_edge("Charpennes\nCharles Hernu", "Brotteaux", weight = 1)
        G.add_edge("Brotteaux", "Gare Part-Dieu\nVivier Merle", weight = 1)
        G.add_edge("Gare Part-Dieu\nVivier Merle", "Place Guichard Bourse\nDu Travail", weight = 2)
        G.add_edge("Place Guichard Bourse\nDu Travail", "Saxe Gambetta", weight = 2)
        G.add_edge("Saxe Gambetta", "Jean Macé", weight = 2)
        G.add_edge("Jean Macé", "Place Jean Jaurès", weight = 2)
        G.add_edge("Place Jean Jaurès", "Debourg", weight = 3)
        G.add_edge("Debourg", "Stade De Gerland", weight = 1)
        G.add_edge("Stade De Gerland", "Oullins Gare", weight = 2)
        G.add_edge("Perrache", "Ampère Victor Hugo", weight = 1)
        G.add_edge("Ampère Victor Hugo", "Bellecour", weight = 1)
        G.add_edge("Bellecour", "Cordeliers", weight = 2)
        G.add_edge("Cordeliers", "Hotel De Ville\nLouis Pradel", weight = 1)
        G.add_edge("Hotel De Ville\nLouis Pradel", "Foch", weight = 2)
        G.add_edge("Foch", "Masséna", weight = 1)
        G.add_edge("Masséna", "Charpennes\nCharles Hernu", weight = 2)
        G.add_edge("Charpennes\nCharles Hernu", "République Villeurbanne", weight = 1)
        G.add_edge("République Villeurbanne", "Gratte-Ciel", weight = 2)
        G.add_edge("Gratte-Ciel", "Flachet", weight = 1)
        G.add_edge("Flachet", "Cusset", weight = 2)
        G.add_edge("Cusset", "Laurent Bonnevay Astroballe", weight = 1)
        G.add_edge("Laurent Bonnevay Astroballe", "Vaulx-En-Velin La Soie", weight = 1)

        path = a_star(G, self.inicio, self.fin, heuristic, modoObjetivo = self.modoObjetivo)
        print("Path: ", path)

        pos = nx.get_node_attributes(G, 'pos')
        plt.figure(figsize=(12, 9))
        nx.draw(G, pos, with_labels=True, node_color="#f86e00", font_size = 7)
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
        plt.xlim(0, 6)
        plt.ylim(0, 7)
        plt.show()



