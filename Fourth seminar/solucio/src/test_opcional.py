##########################################################################
#########   Testos bàsics del seminari 4 de matemàtica discreta   ########
#########              Copyright 2022 Bernat Gastón               ########
#########               Author: Bernat Gastón                     ########
#########            Contact: bernat.gaston@uab.cat               ########
##########################################################################

from main import crea_joc_de_trons
from graph import Graph, Node
from camins import floyd

def test_floyd_simple():
    #Prepare
    #Creem graph buit
    ponent = Graph(False)
    #Creem nodes
    A = Node('Invernalia', 2, 7)
    B = Node('Desembarco del Rey', 3, 3)
    C = Node('Lanza del Sol', 4, 0)
    D = Node("Aguasdulces", 1.5, 4)
    E = Node("Pyke", 0, 4.5)
    
    #Afegim nodes al graph
    ponent.add_node(A)
    ponent.add_node(B)
    ponent.add_node(C)
    ponent.add_node(D)
    ponent.add_node(E)
    #Afegim arestes
    ponent.add_edge(A, B, 4)
    ponent.add_edge(A, C, 8)
    ponent.add_edge(B, C, 1)
    ponent.add_edge(B, D, 2)
    ponent.add_edge(C, D, 4)
    ponent.add_edge(C, E, 2)
    ponent.add_edge(D, E, 7)
    
    expected = [[0, 4, 5, 6, 7], [4, 0, 1, 2, 3], [5, 1, 0, 3, 2], [6, 2, 3, 0, 5], [7, 3, 2, 5, 0]]
    #Execute
    res = floyd(ponent)
    #Assert
    assert res == expected

def test_floyd_dirigit():
    #Prepare
    #Creem graph buit
    ponent = Graph(True)
    #Creem nodes
    A = Node('Invernalia', 2, 7)
    B = Node('Desembarco del Rey', 3, 3)
    C = Node('Lanza del Sol', 4, 0)
    D = Node("Aguasdulces", 1.5, 4)
    E = Node("Pyke", 0, 4.5)
    
    #Afegim nodes al graph
    ponent.add_node(A)
    ponent.add_node(B)
    ponent.add_node(C)
    ponent.add_node(D)
    ponent.add_node(E)
    #Afegim arestes
    ponent.add_edge(A, B, 4)
    ponent.add_edge(A, C, 8)
    ponent.add_edge(B, A, 4)
    ponent.add_edge(B, C, 1)
    ponent.add_edge(B, D, 2)
    ponent.add_edge(C, A, 8)
    ponent.add_edge(C, D, 4)
    ponent.add_edge(C, E, 2)
    ponent.add_edge(D, B, 2)
    ponent.add_edge(D, C, 4)
    ponent.add_edge(D, E, 7)
    ponent.add_edge(E, C, 2)
    ponent.add_edge(E, D, 7)

    expected = [[0, 4, 5, 6, 7], [4, 0, 1, 2, 3], [8, 6, 0, 4, 2], [6, 2, 3, 0, 5], [10, 8, 2, 6, 0]]
    #Execute
    res = floyd(ponent)
    #Assert
    assert res == expected