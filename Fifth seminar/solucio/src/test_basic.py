##########################################################################
#########   Testos bàsics del seminari 4 de grafs i complexitat   ########
#########              Copyright 2022 Bernat Gastón               ########
#########               Author: Bernat Gastón                     ########
#########            Contact: bernat.gaston@uab.cat               ########
##########################################################################

from graph import Graph, Node
from eulerians import hierholzer


def terra_mitja_1():
  #Creem graph buit
    terra_mitja = Graph(False)
    #Creem nodes
    bolson_cerrado = Node('Bolson Cerrado',1,6)
    bree = Node('Bree', 2, 6)
    rivendel = Node('Rivendel', 4, 6)
    lorien = Node('Lorien', 5, 4)
    montaña_solitaria = Node('Montaña Solitaria', 6, 7)
    bosque_negro = Node('Bosque Oscuro', 5, 6)
    puertos_grises = Node('Puertos Grises', 0, 6)
    edoras = Node('Edoras', 5, 1)
    minas_tirith = Node('Minas Tirith', 8, 1)
    #Afegim nodes al graph
    terra_mitja.add_node(rivendel)
    terra_mitja.add_node(bolson_cerrado)
    terra_mitja.add_node(bree)
    terra_mitja.add_node(lorien)
    terra_mitja.add_node(montaña_solitaria)
    terra_mitja.add_node(bosque_negro)
    terra_mitja.add_node(puertos_grises)
    terra_mitja.add_node(edoras)
    terra_mitja.add_node(minas_tirith)
    #Afegim arestes
    terra_mitja.add_edge(bolson_cerrado, bree, 3)
    terra_mitja.add_edge(bree, rivendel, 4)
    terra_mitja.add_edge(edoras, minas_tirith, 6)
    terra_mitja.add_edge(edoras, rivendel, 8)
    terra_mitja.add_edge(lorien, edoras, 4)
    terra_mitja.add_edge(rivendel, lorien, 5)
    terra_mitja.add_edge(lorien, minas_tirith, 7)
    terra_mitja.add_edge(lorien, bosque_negro, 6)
    terra_mitja.add_edge(puertos_grises, edoras, 10)
    terra_mitja.add_edge(puertos_grises, bolson_cerrado, 2)
    terra_mitja.add_edge(rivendel, bosque_negro, 3)
    terra_mitja.add_edge(bosque_negro, minas_tirith, 7)
    terra_mitja.add_edge(bosque_negro, montaña_solitaria, 5)
    terra_mitja.add_edge(montaña_solitaria, minas_tirith, 8)
    return terra_mitja


def terra_mitja_2():
  #Creem graph buit
    terra_mitja = Graph(False)
    #Creem nodes
    bolson_cerrado = Node('Bolson Cerrado',1,6)
    bree = Node('Bree', 2, 6)
    rivendel = Node('Rivendel', 4, 6)
    lorien = Node('Lorien', 5, 4)
    montaña_solitaria = Node('Montaña Solitaria', 6, 7)
    bosque_negro = Node('Bosque Oscuro', 5, 6)
    puertos_grises = Node('Puertos Grises', 0, 6)
    edoras = Node('Edoras', 5, 1)
    minas_tirith = Node('Minas Tirith', 8, 1)
    #Afegim nodes al graph
    terra_mitja.add_node(rivendel)
    terra_mitja.add_node(bolson_cerrado)
    terra_mitja.add_node(bree)
    terra_mitja.add_node(lorien)
    terra_mitja.add_node(montaña_solitaria)
    terra_mitja.add_node(bosque_negro)
    terra_mitja.add_node(puertos_grises)
    terra_mitja.add_node(edoras)
    terra_mitja.add_node(minas_tirith)
    #Afegim arestes
    terra_mitja.add_edge(bolson_cerrado, bree, 3)
    terra_mitja.add_edge(bree, rivendel, 4)
    terra_mitja.add_edge(edoras, minas_tirith, 6)
    terra_mitja.add_edge(edoras, rivendel, 8)
    terra_mitja.add_edge(lorien, edoras, 4)
    terra_mitja.add_edge(rivendel, bosque_negro, 3)
    terra_mitja.add_edge(rivendel, lorien, 5)
    terra_mitja.add_edge(lorien, minas_tirith, 7)
    terra_mitja.add_edge(lorien, bosque_negro, 6)
    terra_mitja.add_edge(puertos_grises, edoras, 10)
    terra_mitja.add_edge(puertos_grises, bolson_cerrado, 2)
    terra_mitja.add_edge(bosque_negro, minas_tirith, 7)
    terra_mitja.add_edge(bosque_negro, montaña_solitaria, 5)
    terra_mitja.add_edge(montaña_solitaria, minas_tirith, 8)
    return terra_mitja


def terra_mitja_3():
  #Creem graph buit
    terra_mitja = Graph(False)
    #Creem nodes
    bolson_cerrado = Node('Bolson Cerrado',1,6)
    bree = Node('Bree', 2, 6)
    rivendel = Node('Rivendel', 4, 6)
    lorien = Node('Lorien', 5, 4)
    montaña_solitaria = Node('Montaña Solitaria', 6, 7)
    bosque_negro = Node('Bosque Oscuro', 5, 6)
    puertos_grises = Node('Puertos Grises', 0, 6)
    edoras = Node('Edoras', 5, 1)
    minas_tirith = Node('Minas Tirith', 7, 0)
    #Afegim nodes al graph
    terra_mitja.add_node(bolson_cerrado)
    terra_mitja.add_node(bree)
    terra_mitja.add_node(rivendel)
    terra_mitja.add_node(lorien)
    terra_mitja.add_node(montaña_solitaria)
    terra_mitja.add_node(bosque_negro)
    terra_mitja.add_node(puertos_grises)
    terra_mitja.add_node(edoras)
    terra_mitja.add_node(minas_tirith)
    #Afegim arestes
    terra_mitja.add_edge(bolson_cerrado, bree, 3)
    terra_mitja.add_edge(bree, rivendel, 4)
    terra_mitja.add_edge(edoras, minas_tirith, 6)
    terra_mitja.add_edge(edoras, rivendel, 8)
    terra_mitja.add_edge(lorien, minas_tirith, 7)
    terra_mitja.add_edge(lorien, edoras, 4)
    terra_mitja.add_edge(puertos_grises, edoras, 10)
    terra_mitja.add_edge(puertos_grises, bolson_cerrado, 2)
    terra_mitja.add_edge(rivendel, bosque_negro, 3)
    terra_mitja.add_edge(rivendel, lorien, 5)
    terra_mitja.add_edge(bosque_negro, montaña_solitaria, 5)
    terra_mitja.add_edge(montaña_solitaria, minas_tirith, 8)
    return terra_mitja


def test_terra_mitja1():
    #Prepare
    terra_mitja = terra_mitja_1()
    checker = terra_mitja_1()
    #Execute
    cami = hierholzer(terra_mitja)
    print(cami)
    print("hooa")
    #Assert
    i = 1
    while i < len(cami):
        node = checker.find_node(cami[i-1].name)
        next_node = checker.find_node(cami[i].name)
        if not node.find_edge(next_node):
            print("El node: " + node.name + " no és veí del node: " + next_node.name)
            assert False
        i = i +1
    print("El camí era:")
    for n in cami:
      print(n.name)
    assert len(cami) == checker.size() + 1


def test_terra_mitja2():
    #Prepare
    terra_mitja = terra_mitja_2()
    checker = terra_mitja_2()
    #Execute
    cami = hierholzer(terra_mitja)
    #Assert
    i = 1
    while i < len(cami):
        node = checker.find_node(cami[i-1].name)
        next_node = checker.find_node(cami[i].name)
        if not node.find_edge(next_node):
            print("El node: " + node.name + " no és veí del node: " + next_node.name)
            assert False
        i = i +1
    print("El camí era:")
    for n in cami:
      print(n.name)
    assert len(cami) == checker.size() + 1


def test_terra_mitja_no_euleria():
    #Prepare
    terra_mitja = terra_mitja_3()
    #Execute
    cami = hierholzer(terra_mitja)
    #Assert
    assert cami == False
