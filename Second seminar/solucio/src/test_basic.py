##########################################################################
#########   Testos bàsics del seminari 2 de grafs i complexitat   ########
#########              Copyright 2022 Bernat Gastón               ########
#########               Author: Bernat Gastón                     ########
#########            Contact: bernat.gaston@uab.cat               ########
##########################################################################

from main import nou_whatsapp, instagram
from graph import Graph, Node

#####################################
####        Testos Exercici 1   #####
#####################################
def test_crea_whatsapp():
    #Prepare
    #Execute
    res = nou_whatsapp()
    #Assert
    assert type(res) == Graph and res.is_directed == False

def test_add_simple_edge():
    #Prepare
    node1 = Node('test1', 0, 0)
    node2 = Node('test2', 0, 1)
    #Execute
    node1.add_simple_edge(node2)
    #Assert
    assert len(node1.edges) == 1

def test_degree_zero():
    #Prepare
    node1 = Node('test1', 0, 0)
    #Execute
    degree = node1.degree()
    #Assert
    assert degree == 0

def test_add_node():
    #Prepare
    graph = Graph()
    node1 = Node('test1', 0, 0)
    #Execute
    graph.add_node(node1)
    #Assert
    assert len(graph.nodes) == 1

def test_delete_node():
    #Prepare
    graph = Graph()
    node1 = Node('test1', 0, 0)
    graph.add_node(node1)
    node2 = Node('test2', 0, 0)
    graph.add_node(node2)
    #Execute
    graph.delete_node(node1)
    #Assert
    assert len(graph.nodes) == 1

def test_add_edge():
    #Prepare
    graph = Graph()
    node1 = Node('test1', 0, 0)
    graph.add_node(node1)
    node2 = Node('test2', 1, 0)
    graph.add_node(node2)
    #Execute
    graph.add_edge(node1, node2)
    #Assert
    assert len(node1.edges) == 1 and len(node2.edges) == 1

def test_order():
    #Prepare
    graph = Graph()
    node1 = Node('test1', 0, 0)
    graph.add_node(node1)
    node2 = Node('test2', 1, 0)
    graph.add_node(node2)
    graph.add_edge(node1, node2)
    #Execute
    res = graph.order()
    #Assert
    assert res == 2



#####################################
####        Testos Exercici 2   #####
#####################################

def test_crea_instagram():
    #Prepare
    #Execute
    res = instagram()
    #Assert
    assert type(res) == Graph and res.is_directed == True


def test_add_directed_edge():
    #Prepare
    node1 = Node('test1', 0, 0)
    node2 = Node('test2', 0, 1)
    #Execute
    node1.add_directed_edge(node2)
    #Assert
    assert len(node1.edges) == 1

def test_neighbours_edge():
    #Prepare
    node1 = Node('test1', 0, 0)
    node2 = Node('test2', 0, 1)
    node1.add_directed_edge(node2)
    #Execute
    res = node1.neighbours()
    #Assert
    assert res == [node2]

def test_size():
    #Prepare
    graph = Graph()
    node1 = Node('test1', 0, 0)
    graph.add_node(node1)
    node2 = Node('test2', 1, 0)
    graph.add_node(node2)
    graph.add_edge(node1, node2)
    #Execute
    res = graph.size()
    #Assert
    assert res == 1

def test_is_neighbour():
        #Prepare
    graph = Graph()
    node1 = Node('test1', 0, 0)
    graph.add_node(node1)
    node2 = Node('test2', 1, 0)
    graph.add_node(node2)
    graph.add_edge(node1, node2)
    #Execute
    res = graph.is_neighbour(node1, node2)
    #Assert
    assert res == True

def test_graphic_sequence():
    #Prepare
    graph = nou_whatsapp()
    #Execute
    res = graph.graphic_sequence()
    #Assert
    assert res == [3,3,2,2,2]