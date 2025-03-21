##########################################################################
#########   Classe main del seminari 2 de grafs i complexitat   ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########    Alumnes: Manel Andreu                              ##########
#########             Arnau Blesa                               ##########
#########             Kevin Palacios                            ##########
##########################################################################


'''
Funció que implementa l'algorisme de havel-hakimi
@param: seq: llista d'enters de la sequència
@return true si és gràfica, false si no.
'''
def havel_hakimi(seq):
    seq.sort(reverse=True)
    while (len(seq) > 2):
        for x in range (0,seq[0]):
            seq[x+1] = seq[x+1]-1
        del seq[0]
        comp=0
        for x in seq:
            if x==0:
                del seq[comp]
            comp+=1
    if seq == [1,1]:
        return True
    else:
        return False