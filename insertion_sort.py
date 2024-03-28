# Uma inserção por vez, assim como algoritmos de ordenação quadrática.

# Podemos fazer uma comparação do Insertion Sort com o modo como algumas pessoas organizam um baralho num jogo de cartas. Imagine que você está jogando ás cartas. Você está com as cartas na mão e elas estão ordenadas. Você recebe uma nova carta e deve colocá-la na posição correta da sua mão de cartas, de forma a que as cartas obedeçam à ordenação.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        carta = lista[i]
        j= i
        while j > 0 and carta < lista[j-1]:
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = carta
    
    print(lista)

insertion_sort([12,3,8,9,6,9,6,10])