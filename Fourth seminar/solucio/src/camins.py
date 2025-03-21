##########################################################################
#########   Funcions del seminari 4 de matemàtica discreta      ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########   Alumnes: Manel Andreu, 1668213                      ##########
#########            Arnau Blesa, 1665951                       ##########
#########            Kevin Palacios, 1671382                    ##########
##########################################################################

import sys


'''
Donades tres llistes retorna l'element de la primera llista que tingui un cost més petit en la segona i que no estigui a la tercera llista
@param: llista de nodes del graf
@param: llista de costos dels nodes
@param: llista de pivots que ja s'han visitat
@return node, min_cost: el node amb cost més petit i el seu cost actual
'''
def troba_min_cost(nodes, costos, pivots):
    min_cost = sys.maxsize
    node = None
    return node, min_cost

'''
Donat un graf i un node inicial, calcula la distancia mínima d'aquest node a tots els altres nodes del graf
@param: node inicial des del que calcular els camins mínims
@return: Exercici 2: llista de costos ordenada segons la llista de nodes del graf.
        Exercici 3: A més dels costos, retorna la llista dels nodes origen del camí mínim
'''

def dijkstraa(node_inicial, graf):
    nodes = graf.nodes
    costos = {node: sys.maxsize for node in nodes}
    recorridos = {node: [] for node in nodes}
    pivots = []

    costos[node_inicial] = 0
    recorridos[node_inicial] = [node_inicial]

    while len(pivots) < len(nodes):
        min_node = None
        min_cost = sys.maxsize

        for node in nodes:
            if node not in pivots and costos[node] < min_cost:
                min_node = node
                min_cost = costos[node]

        pivots.append(min_node)

        for cost, edge in min_node.edges:
            cost_total = min_cost + cost

            if cost_total < costos[edge]:
                costos[edge] = cost_total
                recorridos[edge] = recorridos[min_node] + [edge]

    return list(costos.values()), list(recorridos.values())

'''
Donat un graf, calcula la matriu de camins mínims de qualsevol node a qualsevol altre
@param: graf
@return: Matriu (llista de llistes) amb els valors dels camins mínims
'''
def floyd(graf):
    costos = []
    compt = 0
    for x in range(len(graf.nodes)):
        costos.append([])
        compt2 = 0
        for i in range ((len(graf.nodes))):
            if compt == compt2:
                costos[x].append(0)
            else:
                costos[x].append(100)
            compt2 += 1
        compt += 1
    comptador = 0
    for node in graf.nodes:
        #print('*')
        if graf.is_directed:
            pass
        else:
            for x in node.edges:
                print('-')
                index = graf.nodes.index(x[1])
                costos[comptador][index] = x[0]
                print(comptador,"compt")
                print (index)
                print (x[0], x[1].name)
            comptador+=1
#    comptador = 0
#    num = 1000000
#    for x in costos:
#        compt=0
#        for i in x:
#            if i == 0:
#                pass
#            else:
#                for z in x:
#                    if z == 0:
#                        pass
#                    elif z == '*':
#                        pass
#                    elif z < num:
#                        num=z
#                if int(i) <= (costos[x.index(num)][compt]+min(x)):
#                    pass
#                else:
#                    costos[comptador][compt] = (costos[x.index(num)][compt]+min(x))
#            compt +=1
#        comptador += 1
    print (costos)
    return costos