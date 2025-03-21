##########################################################################
#########   Funció main del seminari 4 de matemàtica discreta   ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########   Alumnes:                                            ##########
##########################################################################

from graph import Node, Graph
from camins import dijkstraa, floyd

'''
Funció que crea un graph simulant Ponent de joc de trons
@return: el graf amb les capitals
'''
def crea_joc_de_trons():
    #Creem graph buit
    ponent = Graph(False)
    #Creem nodes
    invernalia = Node('Invernalia', 2, 7)
    desembarco = Node('Desembarco del Rey', 3, 3)
    lanza_del_sol = Node('Lanza del Sol', 4, 0)
    aguasdulces = Node("Aguasdulces", 1.5, 4)
    pyke = Node("Pyke", 0, 4.5)
    nido_de_aguilas = Node ("Nido de Águilas", 3, 4)
    roca_casterly = Node("Roca Casterly", 0, 3.5)
    altojardin = Node("Altojardín",1 ,2)
    bastion_de_tormentas = Node("Bastión de Tormentas", 4, 2)
    #Afegim nodes al graph
    ponent.add_node(invernalia)
    ponent.add_node(desembarco)
    ponent.add_node(lanza_del_sol)
    ponent.add_node(aguasdulces)
    ponent.add_node(pyke)
    ponent.add_node(nido_de_aguilas)
    ponent.add_node(roca_casterly)
    ponent.add_node(altojardin)
    ponent.add_node(bastion_de_tormentas)
    #Afegim arestes
    ponent.add_edge(invernalia, desembarco, 8)
    ponent.add_edge(invernalia, aguasdulces, 6)
    ponent.add_edge(invernalia, pyke, 3)
    ponent.add_edge(invernalia, bastion_de_tormentas, 9)
    ponent.add_edge(pyke, roca_casterly, 1)
    ponent.add_edge(roca_casterly, aguasdulces, 2)
    ponent.add_edge(aguasdulces, nido_de_aguilas, 2)
    ponent.add_edge(aguasdulces, desembarco, 4)
    ponent.add_edge(desembarco, altojardin, 5)
    ponent.add_edge(desembarco, bastion_de_tormentas, 3)
    ponent.add_edge(desembarco, lanza_del_sol, 7)
    ponent.add_edge(aguasdulces, lanza_del_sol, 5)
    ponent.add_edge(bastion_de_tormentas, lanza_del_sol, 6)
    ponent.add_edge(roca_casterly, altojardin, 5)
    #Dibuxem el graf
    ponent.draw()
    return ponent


if __name__ == '__main__':
    ponent = crea_joc_de_trons()
    node_inicial = ponent.find_node("Invernalia")
    costos = dijkstraa(node_inicial, ponent)
    node_names = [node.name for node in ponent.nodes]
    print(node_names)
    print(costos)