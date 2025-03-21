##########################################################################
#########   Testos bàsics del seminari 2 de grafs i complexitat   ########
#########              Copyright 2022 Bernat Gastón               ########
#########               Author: Bernat Gastón                     ########
#########            Contact: bernat.gaston@uab.cat               ########
##########################################################################

from havelhakimi import havel_hakimi

#####################################
####        Testos Exercici Havel-Hakimi   #####
#####################################

def test_graphic_sequence():
    l = [5,4,3,3,2,2,1]
    val = havel_hakimi(l)
    assert val == True

def test_non_graphic_sequence():
    l = [5,4,3,3,2,2,1,1]
    val = havel_hakimi(l)
    assert val == False