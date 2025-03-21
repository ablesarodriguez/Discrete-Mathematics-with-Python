##########################################################################
#########   Testos bàsics del seminari 4 de grafs i complexitat   ########
#########              Copyright 2022 Bernat Gastón               ########
#########               Author: Bernat Gastón                     ########
#########            Contact: bernat.gaston@uab.cat               ########
##########################################################################

from main import crea_joc_de_trons
from graph import Graph
from camins import dijkstraa

def test_dijkstraa_invernalia():
    #Prepare
    ponent = crea_joc_de_trons()
    node_inicial = ponent.find_node("Invernalia")
    node_names = [node.name for node in ponent.nodes]
    expected = {
        "Invernalia": 0,
        'Desembarco del Rey': 8,
        'Lanza del Sol':  11,
        "Aguasdulces": 6,
        "Pyke": 3,
        "Nido de Águilas": 8,
        "Roca Casterly": 4,
        "Altojardín": 9,
        "Bastión de Tormentas": 9,
    }
    #Execute
    costos, recorreguts = dijkstraa(node_inicial, ponent)
    #Assert
    res = {node_names[i]: costos[i] for i in range(len(node_names))}
    assert res == expected

def test_dijkstraa_desembarco():
    #Prepare
    ponent = crea_joc_de_trons()
    node_inicial = ponent.find_node("Desembarco del Rey")
    node_names = [node.name for node in ponent.nodes]
    expected = {
        "Invernalia": 8,
        'Desembarco del Rey': 0,
        'Lanza del Sol':  7,
        "Aguasdulces": 4,
        "Pyke": 7,
        "Nido de Águilas": 6,
        "Roca Casterly": 6,
        "Altojardín": 5,
        "Bastión de Tormentas": 3,
    }
    #Execute
    costos, recorreguts = dijkstraa(node_inicial, ponent)
    #Assert
    res = {node_names[i]: costos[i] for i in range(len(node_names))}
    assert res == expected