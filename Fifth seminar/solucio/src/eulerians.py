##################################################################################
#########   Funcions eulerianes del seminari 4 de grafs i complexitat   ##########
#########                     Copyright 2022 Bernat Gastón              ##########
#########                      Author: Bernat Gastón                    ##########
#########                   Contact: bernat.gaston@uab.cat              ##########
#########   Alumnes:  Kevin Palacios Parada  1671382                    ##########
#########             Arnau Blesa            1665951                    ##########
#########             Manel Andreu Vidal     1668213                    ##########
##################################################################################

'''
Donat una llista de nodes retorna el primer node de grau més gran que zero
@param El graf
@return El node trobat. False si no troba cap node candidat
'''
def get_init_node(graph):
    for node in graph.nodes:
        if node.degree() == True:
            return node
    return False

'''
Donat una llista de nodes retorna el primer node de grau més gran que zero
@param circuit: La llista de node
@return El node trobat. False si no en troba cap.
'''
def get_next_node(circuit):
    for node in circuit:
        if node.degree() == True:
            return node
    return False

'''
Troba un cami/circuit eulerià donat un graf. Primer comprova que existeixi el cami, després aplica l'algorisme de hierholzer.
@param graph: el graf
@return Una llista amb el cami/circuit eulerià
'''
def hierholzer(graph):
    ''' Comprovació de l'existencia d'un circuit eulerià. '''
    comptador = 0
    for node in graph.nodes:
        grau = node.degree()
        if grau % 2 == 0:
            pass
        else:
            comptador += 1
    if comptador == 0:
        pass
    else:
        return False
    ''' Creació cami eulerià '''
    cami_euleria = []
    cami_euleria2 = []

    nodes = graph.nodes
    node = nodes[0]
    acabar = 0
    ''' Omplim primer amb 1 aresta'''
    cami_euleria2.append(node)
    veins = node.neighbours()
    cami_euleria2.append(veins[0])
    node.remove_edge(veins[0])
    veins[0].remove_edge(node)
    ''' omplir cami_euleria'''
    while True:
        ''' Agafem l'ultim node visitat i obtenim els veïns per escollir-ne el primer'''
        ultim = cami_euleria2[-1]
        veins = ultim.neighbours()
        ''' Mirem si hi ha veins, si no hi han ampliem cami_euleria amb cami_euleria2 i busquem un nou node amb veïns'''
        if len(veins) == 0:
            if len(cami_euleria) == 0:
                cami_euleria = cami_euleria2
                cami_euleria2 = []
            else:
                llista=[]
                llista.extend(cami_euleria[:(posicio)])
                llista.extend(cami_euleria2)
                llista.extend(cami_euleria[(posicio+1):])
                cami_euleria = llista
                cami_euleria2 = []
            for x in cami_euleria:
                veins = x.neighbours()
                if len(veins) > 0:
                    for z in veins:
                        print (z.name, "vecino")
                    print ("sdadsadsasd")
                    acabar = 0
                    posicio = cami_euleria.index(x)
                    ultim = x
                    cami_euleria2.append(ultim)
                    break
                else:
                    acabar = 1
            ''' Si no hi han finalitzem'''
            if acabar == 1:
                return cami_euleria
        ''' Si hi han veïns agafem el primer i l'afegim a cami_euleria2'''
        cami_euleria2.append(veins[0])
        ultim.remove_edge(veins[0])
        veins[0].remove_edge(ultim)