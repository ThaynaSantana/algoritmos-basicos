
def quick_sort(lista):
    tamanho = len(lista)
    # determinando que o pivo sera o numero "do meio" da lista
    pivo = lista[tamanho//2]
    esquerda, direita = [], []
    for n in lista:
        if n <= pivo:
            esquerda.append(n)
        elif n > pivo:
            direita.append(n)
    # ordenando a lista direita(maiores numeros)
    direita.sort()
    # ordenando a lista esquerda(menores numeros)
    esquerda.sort()
    # Lista final totalmente ordenada
    lista_ordenada = esquerda+direita
    print(lista_ordenada)
    return lista_ordenada

quick_sort([6,3,4,7,8,2,5])