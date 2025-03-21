##########################################################################
#########          Testos bàsics del seminari 3 de MD           ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########   Alumnes: Manel Andreu, 1668213                      ##########
#########            Arnau Blesa, 1665951                       ##########
#########            Kevin Palacios, 1671382                    ##########
##########################################################################

from main import crea_internet
from graph import Graph, Node
from cerques import BFS, DFS

def test_crea():
    #Prepare
    #Execute
    res = crea_internet()
    #Assert
    assert type(res) == Graph

def test_find_node():
    #Prepare
    internet = crea_internet()
    #Execute
    res = internet.find_node('JocsiEsport')
    #Assert
    assert res.name == 'JocsiEsport'

def test_BFS():
    #Prepare
    internet = crea_internet()
    node_inicial = internet.find_node('JocsiEsport')
    nivells = {
        'JocsiEsport': 0,
        'TotJocs': 1,
        'SPORT': 1,
        'MARCA': 1,
        'AS': 1,
        'NBATotal': 2,
        'LOLFans': 2,
        'AmongUsEurope': 2,
        'LOLCommunity': 3
    }
    #Execute
    res_list = BFS(node_inicial)
    #Assert
    nivell_actual = 0
    print('\n')
    for node in res_list:
        print(node.name)
        if nivells[node.name] == nivell_actual:
            continue
        if nivells[node.name] == nivell_actual + 1:
            nivell_actual = nivell_actual + 1
        else:
            assert False
    assert True

def test_DFS():
    #Prepare
    internet = crea_internet()
    node_inicial = internet.find_node('JocsiEsport')
    nivells = {
        'JocsiEsport': 0,
        'TotJocs': 1,
        'SPORT': 1,
        'MARCA': 1,
        'AS': 1,
        'NBATotal': 2,
        'LOLFans': 2,
        'AmongUsEurope': 2,
        'LOLCommunity': 3
    }
    #Execute
    res_list = DFS(node_inicial)
    #Assert
    nivell_actual = 0
    print('\n')
    for node in res_list:
        print("Nivell actual: " + str(nivell_actual))
        print(node.name)
        if nivells[node.name] == nivell_actual:
            nivell_actual = nivell_actual + 1
        elif nivells[node.name] > nivell_actual:
            assert False
        elif nivells[node.name] < nivell_actual:
            nivell_actual = nivells[node.name] + 1
    assert True

def test_dibujar():
    internet = crea_internet()
    node = internet.find_node('JocsiEsport')
    print('\n', node)
