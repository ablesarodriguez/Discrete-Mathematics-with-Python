##########################################################################
#########   Testos avançats del seminari 1 de grafs i complexitat ########
#########              Copyright 2022 Bernat Gastón               ########
#########               Author: Bernat Gastón                     ########
#########            Contact: bernat.gaston@uab.cat               ########
##########################################################################


from aprova import fes_examens_descarta_opcions
from pytest import approx

def test_deu_nou_quatre():
    #Prepare
    #Execute
    res = fes_examens_descarta_opcions(10,9,[2],4)
    #Assert Deberia ser igual a 1
    assert res*100 == approx(100.0, rel=0.9)

def test_deu_cinc_quatre():
    #Prepare
    #Execute
    res = fes_examens_descarta_opcions(10,5,[2,2,2,2,2],4)
    #Assert 
    assert res*100 == approx(81.0, rel=0.9)

def test_deu_quatre_quatre():
    #Prepare
    #Execute
    res = fes_examens_descarta_opcions(10,4,[2,3,3,2],4)
    #Assert 
    assert res*100 == approx(55.0, rel=0.9) 

def test_deu_zero_quatre():
    #Prepare
    #Execute
    res = fes_examens_descarta_opcions(10,0,[2,3,4,2,3,4,3,4,3,4],4)
    #Assert 0.0
    assert res*100 == approx(1.7, rel=0.9)