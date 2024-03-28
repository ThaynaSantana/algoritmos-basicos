
def fibonacci(number):
    if number < 0:
        raise Exception("Numero precisa ser positivo e inteiro")
    
    sequencia=[0]
    prev, curr = 0,1

    for i in range(number):
        sequencia.append(curr)
        curr, prev = curr + prev, curr

    print(sequencia)
    return sequencia

fibonacci(9)