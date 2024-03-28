# Ordenação por seleção, baseado em se passar sempre o menor valor
# do vetor para primeira posição(ou do maior dependendo da ordem requerida),
# com os n-1

def selection_sort(lista):
    for i in range(len(lista)):
        menor = i

        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        
        if lista[i] != lista[menor]:
            prev = lista[i]
            lista[i], lista[menor] = lista[menor], prev

    print(lista)


selection_sort([9,6,2,0,1])