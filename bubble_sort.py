# A ideia é percorrer um conjunto de elementos diversas vezes, e a cada passagem fazer flutuar para o topo o maior elemento da sequência. 

# não é recomendado para programas que precisem
# de velocidade e operem com quantidade elevada de dados.

def bubble_sort(lista: list):
    tamanho = len(lista)
    i=0
    j=0
    for i in range(tamanho):
        for j in range(tamanho - 1):
            if lista[j] < lista[j+1]:
                prev = lista[j]
                lista[j], lista[j+1] = lista[j+1], prev

    print(lista)
    return lista