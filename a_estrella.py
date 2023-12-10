from heapq import heappop, heappush
import datetime as dt

def a_star(grafo, nodoInicio, nodoObjetivo, heuristica, horaSalida):
    listaBusqueda = [(0, None, nodoInicio, 0, horaSalida)] #CosteF, Linea, Nodo, transbordos
    costeG = {nodoInicio: 0}
    costeF = {nodoInicio: 0}
    caminoAnterior = {nodoInicio: None}

    while listaBusqueda:
        #Elige el nodo con el coste menor
        _, lineaActual, nodoActual, transbordos, hora = heappop(listaBusqueda)

        #Si el nodo es el nodo Objetivo, hemos terminado y
        #devolvemos el camino que nos ha llevado hasta el
        if nodoActual == nodoObjetivo:
            camino = []
            while nodoActual is not None:
                camino.append(nodoActual)
                nodoActual = caminoAnterior[nodoActual]
            camino.reverse()
            return [camino, hora]

        #Recorremos todos los vecinos del grafo
        for nodoVecino in grafo.neighbors(nodoActual):
            #Calculamos el coste de ir desde el nodo actual hasta el vecino
            costeGVecino = costeG[nodoActual] + grafo.edges[nodoActual, nodoVecino]['weight']
            h, transbordosAux, variacionTiempo = heuristica(nodoVecino, nodoObjetivo, nodoActual, lineaActual, transbordos, hora)
            if(h==-1):
                return [-1, 0]
            costeFVecino = costeGVecino + h
            #Miramos si el camino actual es mejor que el anterior o si el vecino no ha sido visitado
            if nodoVecino not in costeG or costeFVecino < costeF[nodoVecino]:
                #Actualizamos el coste del vecino
                costeG[nodoVecino] = costeGVecino
                costeF[nodoVecino] = costeFVecino
                #Actualizamos la hora de llegada al nodo vecino
                horaAux = hora + variacionTiempo + dt.timedelta(minutes = grafo.edges[nodoActual, nodoVecino]['weight'])
                #Linea en comun entre nodoActual y nodoVecino
                lineaAux = str((set(grafo.nodes[nodoVecino]['linea']) & set(grafo.nodes[nodoActual]['linea']) ).pop())
                #Añadimos el vecino a la lista de busqueda
                heappush(listaBusqueda, (costeFVecino, lineaAux,nodoVecino,transbordosAux,horaAux))
                #Guardamos el camino que nos ha llevado hasta el vecino
                caminoAnterior[nodoVecino] = nodoActual

    return None