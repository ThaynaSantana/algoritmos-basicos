from bubble_sort import bubble_sort

def test_ordenacao_bubble_sort():
    lista = [30,9,4,1,123,80]
    assert bubble_sort(lista) == [123,80,30,9,4,1]