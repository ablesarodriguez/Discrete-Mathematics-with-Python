##########################################################################
#########   Classe aprova del seminari 1 de grafs i complexitat   ########
#########              Copyright 2022 Bernat Gastón               ########
#########               Author: Bernat Gastón                     ########
#########            Contact: bernat.gaston@uab.cat               ########
#########            Alumnes: Manel Andreu, 1668213               ########
#########                     Arnau Blesa, 1665951                ########
##########################################################################

from random import randint


'''
Funció que genera dos nombres aleatoris entre 1 i num_opcions i els compara. Retorna True si son iguals, False si no ho son.
Simula una resposta aleatoria
@param: número de opcions
@return: True si els nombres son iguals, False si no
'''
def resposta_pregunta(num_opcions):
    num1= randint(1, num_opcions)
    num2 = randint(1, num_opcions)
    iguals = False

    if num1 == num2:
        iguals = True
    return iguals

'''
Funció que donat un examen de tipus test, calcula les probabilitats d'aprovar empíricament. 
Assumeix que totes les preguntes valen igual, que l'exàmen és sobre 10 i que les preguntes
resten de forma equivalent
@param: num_preguntes: Número de preguntes totals del exàmen
@param num_preguntes_resposes: Número de preguntes correctament resposes
@param num_preguntes_aleatories: Número de preguntes que respondrem aleatoriament
@param num_opcions: Número d'opcions per pregunta
@return nombre entre 0 i 1
'''


def fes_examens(num_preguntes, num_preguntes_resposes, num_preguntes_aleatories, num_opcions):
    valor_pregunta = 10 / num_preguntes
    resta_pregunta = valor_pregunta / (num_opcions - 1)
    num_aprovades = 0

    for j in range(0, 100000):
        correctes = 0
        incorrectes = 0
        for i in range(num_preguntes_aleatories):
            if resposta_pregunta(num_opcions):
                correctes += 1
            else:
                incorrectes += 1

        nota = valor_pregunta * (num_preguntes_resposes + correctes) - resta_pregunta * incorrectes

        if nota >= 5:
            num_aprovades += 1

    return num_aprovades/100000

'''
OPCIONAL Funció que donat un examen de tipus test, calcula les probabilitats d'aprovar empíricament. 
Assumeix que totes les preguntes valen igual, que l'exàmen és sobre 10 i que les preguntes
resten de forma equivalent.
@param: num_preguntes: Número de preguntes total del exàmen
@param num_preguntes_resposes: Número de preguntes correctament resposes
@param preguntes_aleatories: Llista amb el nombre d’opcions en les quals dubteu per a cada pregunta aleatòria
@param num_opcions: Número d'opcions per pregunta
'''
def fes_examens_descarta_opcions(num_preguntes, num_preguntes_resposes, preguntes_aleatories, num_opcions):
    valor_pregunta = 10 / num_preguntes
    resta_pregunta = valor_pregunta / (num_opcions - 1)
    num_aprovades = 0

    for i in range(0, 100000):
        correctes = 0
        incorrectes = 0
        for j in range(0, len(preguntes_aleatories)):
            if resposta_pregunta(num_opcions):
                correctes += 1
            else:
                incorrectes += 1

        nota = valor_pregunta * (num_preguntes_resposes + correctes) - resta_pregunta * incorrectes

        if nota >= 5:
            num_aprovades += 1

    return num_aprovades / 100000
