from heapq import heappop, heappush
from itertools import count

import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.shortest_paths.weighted import _weight_function


def a_star(grafo, nodoInicio, nodoObjetivo, heuristica, modoObjetivo = None):
    listaBusqueda = [(0, None, nodoInicio)]
    costeG = {nodoInicio: 0}
    caminoAnterior = {nodoInicio: None}

    while listaBusqueda:
        #Elige el nodo con el coste menor
        _, lineaActual, nodoActual = heappop(listaBusqueda)

        if nodoActual == nodoObjetivo:
            camino = []
            while nodoActual is not None:
                camino.append(nodoActual)
                nodoActual = caminoAnterior[nodoActual]
            camino.reverse()
            return camino

        for nodoVecino in grafo.neighbors(nodoActual):
            #Calculamos el coste de ir desde el nodo actual hasta el vecino
            aumentoCoste_G = costeG[nodoActual] + grafo.edges[nodoActual, nodoVecino]['weight']

            #Miramos si el camino actual es mejor que el anterior
            if nodoVecino not in costeG or aumentoCoste_G < costeG[nodoVecino]:
                costeG[nodoVecino] = aumentoCoste_G
                costeF = aumentoCoste_G + heuristica(nodoVecino, nodoObjetivo, nodoActual, lineaActual)
                lineaActual = set(grafo.nodes[nodoVecino]['linea']) & set(grafo.nodes[nodoActual]['linea']) #esta linea es GOD
                heappush(listaBusqueda, (costeF, lineaActual,nodoVecino))
                caminoAnterior[nodoVecino] = nodoActual

    return None

# Implementacion del algoritmo A*
def a_estrella_ruta(G, source, target, heuristica=None, weight="weight", modoObjetivo = None):

    # Se verifica que los nodos esten en el grafo
    if source not in G or target not in G:
        raise nx.NodeNotFound(f"El nodo origen: {source} o el nodo nodoObjetivo: {target} no estan en el grafo.")

    # Se verifica que el peso sea positivo
    if heuristica is None:
        def heuristica(u, v):
            return 0

    weight = _weight_function(G, weight)

    G_succ = G._adj

    c = 0
    queue = [(0, c, source, 0, None)]
    enqueued = {}
    explored = {}

    while queue:

        _, __, curnode, dist, nodoPadre = heappop(queue)

        if curnode == target:
            path = [curnode]
            node = nodoPadre
            while node is not None:
                path.append(node)
                node = explored[node]
            path.reverse()
            return path

        if curnode in explored:
            if explored[curnode] is None:
                continue

            qcost, h = enqueued[curnode]
            if qcost < dist:
                continue
        
        explored[curnode] = nodoPadre

        #Recorremos la tabla de adyacencia del nodo actual
        for neighbor, w in G_succ[curnode].items():
            coste = weight(curnode, neighbor, w)
            #Los nodos que no estan conectados no se consideran
            if coste is None:
                continue
            ncost = dist + coste
            if neighbor in enqueued:
                qcost, h = enqueued[neighbor]
                if qcost <= ncost:
                    continue
            else:
                h = heuristica(neighbor, target, modoObjetivo)
            enqueued[neighbor] = ncost, h
            c += 1
            heappush(queue, (ncost + h, c, neighbor, ncost, curnode))
            
    raise nx.NetworkXNoPath(f"El nodo: {target} no se puede alcanzar desde: {source}")
