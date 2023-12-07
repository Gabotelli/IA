from heapq import heappop, heappush

def a_star(grafo, nodoInicio, nodoObjetivo, heuristica, modoObjetivo = None):
    listaBusqueda = [(0, None, nodoInicio, 0)] #CosteF, Linea, Nodo, transbordos
    costeG = {nodoInicio: 0}
    costeF = {nodoInicio: 0}
    caminoAnterior = {nodoInicio: None}

    while listaBusqueda:
        #Elige el nodo con el coste menor
        _, lineaActual, nodoActual, transbordos = heappop(listaBusqueda)

        #Si el nodo es el nodo Objetivo, hemos terminado y
        #devolvemos el camino que nos ha llevado hasta el
        if nodoActual == nodoObjetivo:
            camino = []
            while nodoActual is not None:
                camino.append(nodoActual)
                nodoActual = caminoAnterior[nodoActual]
            camino.reverse()
            return camino

        #Recorremos todos los vecinos del grafo
        for nodoVecino in grafo.neighbors(nodoActual):
            #Calculamos el coste de ir desde el nodo actual hasta el vecino
            costeGVecino = costeG[nodoActual] + grafo.edges[nodoActual, nodoVecino]['weight']
            h, transbordosAux= heuristica(nodoVecino, nodoObjetivo, nodoActual, lineaActual, transbordos)
            costeFVecino = costeGVecino + h
            #Miramos si el camino actual es mejor que el anterior o si el vecino no ha sido visitado
            if nodoVecino not in costeG or costeFVecino < costeF[nodoVecino]:
                #Actualizamos el coste del vecino
                costeG[nodoVecino] = costeGVecino
                costeF[nodoVecino] = costeFVecino
                #Linea en comun entre nodoActual y nodoVecino
                lineaAux = str((set(grafo.nodes[nodoVecino]['linea']) & set(grafo.nodes[nodoActual]['linea']) ).pop())
                #Añadimos el vecino a la lista de busqueda
                heappush(listaBusqueda, (costeFVecino, lineaAux,nodoVecino,transbordosAux))
                #Guardamos el camino que nos ha llevado hasta el vecino
                caminoAnterior[nodoVecino] = nodoActual

    return None