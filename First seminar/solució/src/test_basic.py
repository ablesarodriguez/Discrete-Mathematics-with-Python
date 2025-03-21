##########################################################################
#########   Testos bàsics del seminari 1 de grafs i complexitat   ########
#########              Copyright 2022 Bernat Gastón               ########
#########               Author: Bernat Gastón                     ########
#########            Contact: bernat.gaston@uab.cat               ########
##########################################################################

from aprova import fes_examens
from pytest import approx

def test_deu_sis_quatre_quatre():
    #Prepare
    #Execute
    res = fes_examens(10,6,4,4)
    #Assert
    assert res*100 == approx(68.35, rel=0.9)

def test_deu_zero_deu_quatre():
    #Prepare
    #Execute
    res = fes_examens(10,0,10,4)
    #Assert
    assert res*100 == approx(0.32, rel=0.9)

def test_deu_sis_una_quatre():
    #Prepare
    #Execute
    res = fes_examens(10,6,1,4)
    #Assert
    assert res*100 == approx(100, rel=0.9)

