##########################################################################
#########   Funció main del seminari 5 de grafs i complexitat   ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########   Alumnes:                                            ##########
##########################################################################

from graph import Node, Graph
from eulerians import hierholzer

'''
Funció que crea un graph simulant Ponent de joc de trons
@return: el graf amb les capitals
'''
def crea_terra_mitja():
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

    #Dibuxem el graf
    terra_mitja.draw()
    return terra_mitja

if __name__ == '__main__':
    terra_mitja = crea_terra_mitja()
    cami_euleria = hierholzer(terra_mitja)
    print("Cami Eulerià:")
    for n in cami_euleria:
      print(n.name)