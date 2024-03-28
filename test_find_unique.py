# Testes do algorimo fin_unique
import sys
import pytest

from find_unique import find_unique

def test_se_encontra_o_unico_numero_que_nao_repete():
    lista=[1,1,2,2,7,8,8,0,0]
    assert find_unique(lista) == [7]

def test_se_encontra_numero_unico_no_meio_repeticao():
    lista=[5,5,6,4,6,7,7]
    assert find_unique(lista) == [4]

def test_se_mesmo_numero_repetido_encontra_o_unico():
    lista=[0,0,0,0,0,0,2,0]
    assert find_unique(lista) == [2]

def test_se_com_mais_numeros_repetidos_se_encontra():
    lista=[0,1,1,0,2,3,7,7,2,9,4]
    assert find_unique(lista) == [3,9,4]