##########################################################################
#########            Funció main del seminari 3 de MD           ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########   Alumnes: Manel Andreu, 1668213                      ##########
#########            Arnau Blesa, 1665951                       ##########
#########            Kevin Palacios, 1671382                    ##########
##########################################################################

from graph import Node, Graph
from cerques import BFS, DFS

'''
Funció que crea un graf simulant una mini internet
@return: el graf creat
'''
def crea_internet():
    inter = Graph()
    inter.is_directed = True
    nodes = [Node('JocsiEsport', 1, 1), Node('AmongUsEurope', 0, 0), Node('LOLFans', 0, 1), Node('TotJocs', 1, 0),
             Node('LOLCommunity', 2, 0), Node('MARCA', 2, 1), Node('AS', 0, 2), Node('NBATotal', 1, 2),
             Node('SPORT', 2, 2)]
    for i in nodes:
        inter.add_node(i)

    c = [[0, 0, 0, 1, 0, 1, 1, 0, 1],
         [0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 0, 0, 0, 0],
         [0, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0]]
    i = 0
    while (i < len(nodes)):
        j = 0
        while (j < len(nodes)):
            if (c[i][j] == 1):
                inter.add_edge(nodes[i], nodes[j])
            j += 1
        i += 1
    return inter

if __name__ == '__main__':
    internet = crea_internet()
