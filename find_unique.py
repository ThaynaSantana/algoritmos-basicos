# Escreva uma função 'find_unique' que encontre o unico
# elemento não repetido em uma lista onde todos outros
# aparecem duas vezes

def find_unique(array):
    numeros_unicos=[]
    for numero in array:
        if array.count(numero) == 1:
            numeros_unicos.append(numero)

    return numeros_unicos

find_unique([1,1,6,8,9,8,9,0,0,2,2])