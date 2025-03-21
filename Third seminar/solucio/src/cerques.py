##########################################################################
#########               Funcions del seminari 3 de MD           ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########   Alumnes: Manel Andreu, 1668213                      ##########
#########            Arnau Blesa, 1665951                       ##########
#########            Kevin Palacios, 1671382                    ##########
##########################################################################

from collections import deque

'''
Donat un node inicial en un graf, descobreix el graf mitjançant l'algorisme BFS
@param: Node inicial
@return: llista de nodes visitats
'''
def BFS(init_node):
    visitades = []
    pendents = deque()
    pendents.append(init_node)

    while pendents:
        node = pendents.popleft()

        if node not in visitades:
            visitades.append(node)
            neighbors = node.edges

            for neighbor in neighbors:
                pendents.append(neighbor)

    return visitades

'''
Donat un node inicial en un graf, descobreix el graf mitjançant l'algorisme DFS
@param: Node inicial
@return: llista de nodes visitats
'''
def DFS(init_node):
    llista = []
    llista.append(init_node)
    b = init_node.neighbours()
    llista.extend(b)

    for x in b:
        if x not in llista:
            llista.append(x)

        a = x.neighbours()

        for i in a:
            if i not in llista:
                llista.append(i)

    print('\n')
    for x in llista:
        print(x.name)

    return llista
