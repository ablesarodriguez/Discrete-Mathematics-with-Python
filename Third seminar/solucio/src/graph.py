##########################################################################
#########           Classe Graph del seminari 3 de MD           ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########   Alumnes: Manel Andreu, 1668213                      ##########
#########            Arnau Blesa, 1665951                       ##########
#########            Kevin Palacios, 1671382                    ##########
##########################################################################

import matplotlib.pyplot as plt
from math import trunc

'''
Classe que crea un Node de un graf
'''
class Node:
    '''
    Constructor de classe
    VE DEL SEMINARI 2   
    @param: name: nom del node
    @param: x: posició del node en x al gràfic
    @param: y: posició del node en y al gràfic
    '''
    def __init__(self, name, x=0, y=0) -> None:
        self.name = name
        self.edges = list()
        self.set_pose(x, y)
    
    '''
    Redefineix la posició d'un node
    VE DEL SEMINARI 2   
    @param: x: posició del node en x al gràfic
    @param: y: posició del node en y al gràfic
    '''    
    def set_pose(self, x, y):
        self.x = x
        self.y = y

    '''
    Calcula el grau d'un node
    VE DEL SEMINARI 2   
    @return: Grau del node
    '''
    def degree(self):
        return len(self.edges)

    '''
    Afegeix una aresta simple. 
    Cal tenir en compte que una aresta simple significa que els dos nodes conectats tenen al altre com a veí
    VE DEL SEMINARI 2
    @param: node: el node amb el que afegir la aresta
    '''
    def add_simple_edge(self, node):
        self.edges.append(node)
        node.edges.append(self)
    
    '''
    Afegeix una aresta dirigida
    VE DEL SEMINARI 2   
    @param: node: el node amb el que afegir la aresta
    '''
    def add_directed_edge(self, node):
        self.edges.append(node)

    '''
    Retorna els veins del node
    VE DEL SEMINARI 2  
    @retorn una llista amb els nodes veins
    '''
    def neighbours(self):
        return self.edges

    '''
    Dibuixa el node amb les seves arestes (només per Graf dirigit)
    VE DEL SEMINARI 2   
    '''
    def draw_directed(self):
        plt.plot(self.x, self.y, marker='o', markerfacecolor='blue', markersize=12)
        plt.annotate(self.name, (self.x-0.1, self.y+0.1))
        for vei in self.edges:
            dx = vei.x-self.x
            dy = vei.y-self.y
            plt.arrow(self.x, self.y, dx, dy, width=0.001, 
            head_width=0.15, head_length=0.2, facecolor='green', length_includes_head=True)


    '''
    Dibuixa el node amb les seves arestes (només per Graf simple)
    VE DEL SEMINARI 2   
    '''
    def draw_simple(self):
        for vei in self.edges:
            x = [self.x]
            y = [self.y]
            if self in vei.edges:
                x.append(vei.x)
                y.append(vei.y)
            plt.plot(x, y, color='green', marker='o', markerfacecolor='blue', markersize=12)
        plt.annotate(self.name, (self.x- 0.05, self.y+0.05))

'''
Classe que representa un graf
'''
class Graph:
    '''
    Constructor que crea un graf buit
    VE DEL SEMINARI 2
    @param: id_directed: True si el graph és dirigit, False si no
    '''
    def __init__(self, is_directed=False) -> None:
        self.nodes = list()
        self.is_directed = is_directed

    '''
    Afegeix un node al graf
    VE DEL SEMINARI 2
    @param: node: Node a afegir
    '''
    def add_node(self, node):
        self.nodes.append(node)

    '''
    Treu un node del graf
    VE DEL SEMINARI 2
    '''
    def delete_node(self, node):
        self.nodes.remove(node)

    '''
    Crea una aresta entre dos nodes. Depen de quin tipus de graf tenim
    VE DEL SEMINARI 2   
    @param: node1: primer node
    @param node2: segon node
    '''
    def add_edge(self, node1, node2):
        if self.is_directed:
            node1.add_directed_edge(node2)
        else:
            node1.add_simple_edge(node2)

    '''
    Calcula l'ordre del graf
    VE DEL SEMINARI 2   
    @return: L'ordre del graf
    '''
    def order(self):
        return len(self.nodes)

    '''
    Calcula la mida d'un graf
    VE DEL SEMINARI 2   
    return: La mida del graf
    '''
    def size(self):
        size = 0
        for node in self.nodes:
            size = size + len(node.edges)
        if not self.is_directed:
            size = trunc(size/2)
        return size

    '''
    Comprova si dos nodes son veins. Si és dirigit, només calcula si es pot arribar al segon node desde el primer
    VE DEL SEMINARI 2   
    @param node1: Primer node
    @param node2: Segon node
    '''
    def is_neighbour(self, node1, node2):
        if node2 in node1.neigbours():
            return True
        else:
            return False

    '''
    Calcula la sequència gràfica del graf
    VE DEL SEMINARI 2   
    @return: La sequència gràfica (ordenada de major a menor)
    '''
    def graphic_sequence(self):
        graphic_seq = list()
        for node in self.nodes:
            graphic_seq.append(node.degree())
        graphic_seq.sort(reverse = True)
        return graphic_seq

    '''
    Donat un nom, busca i retorna el node que hi conincideix
    @param: name: el nom del node a buscar
    @return: El node si el troba, None si no.
    '''
    def find_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None


    '''
    Dibuixa el graf
    VE DEL SEMINARI 2   
    '''
    def draw(self):
        for node in self.nodes:
            if self.is_directed:
                node.draw_directed()
            else:
                node.draw_simple()
        plt.show()