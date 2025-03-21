##########################################################################
#########   Classe main del seminari 2 de grafs i complexitat   ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########    Alumnes: Manel Andreu                              ##########
#########             Arnau Blesa                               ##########
#########             Kevin Palacios                            ##########
##########################################################################

from graph import Node, Graph
from havelhakimi import havel_hakimi

'''
Funció del exercici 1 per modelar el nou whatsapp amb les relacions donades.
@retorn: El graf representant les relacions donades
'''
def nou_whatsapp():
    whatsapp = Graph()
    nodes = [Node('Teresa', 1, 4), Node('Jana', 2, 7), Node('Ariadna', 6, 6), Node('Joan', 7, 2), Node('Pau', 4, 1)]
    for i in nodes:
        whatsapp.add_node(i)

    c = [[0, 1, 1, 1, 1], [1, 0, 1, 0, 0], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0]]
    i = 0
    while (i<len(nodes)):
        j = 0
        while (j<len(nodes)):
            if (c[i][j] == 1 and c[j][i] == 1):
                whatsapp.add_edge(nodes[i], nodes[j])
            j += 1
        i += 1

    return whatsapp

'''
Funció del exercici 2 per modelar el instagram amb les relacions donades.
@retorn: El graf representant les relacions donades.
'''

def instagram():
    insta = Graph()
    insta.is_directed = True
    nodes = [Node('Teresa', 1, 4), Node('Jana', 2, 7), Node('Ariadna', 6, 6), Node('Joan', 7, 2), Node('Pau', 4, 1)]
    for i in nodes:
        insta.add_node(i)

    c = [[0, 1, 1, 1, 1], [1, 0, 1, 0, 0], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0]]
    i = 0
    while (i < len(nodes)):
        j = 0
        while (j < len(nodes)):
            if (c[i][j] == 1):
                insta.add_edge(nodes[i], nodes[j])
            j += 1
        i += 1

    return insta



if __name__ == '__main__':
    #Creem un graf buit
    graph = Graph()
    #Creeem nodes
    node1 = Node('node1', 0, 0)
    node2 = Node('node2', 1, 1)
    #Afegir nodes al graf
    graph.add_node(node1)
    graph.add_node(node2)
    #Afegir arestes
    graph.add_edge(node1, node2)
    #Dibuixem el graf
    graph.draw()
