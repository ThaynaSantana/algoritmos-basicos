from quick_sort import quick_sort

def test_quick_sort_array_simple():
    lista=[8,6,4,2,9]
    assert quick_sort(lista) == [2,4,6,8,9]

def test_quick_sort_repeated_numberes():
    lista=[9,2,4,5,7,123,4,4,10]
    assert quick_sort(lista) == [2,4,4,4,5,7,9,10,123]

def test_quick_sort_same_number():
    lista=[0,0,0,0,0,0]
    assert quick_sort(lista) == [0,0,0,0,0,0]

def test_quick_sort_number_equal_to_pivot():
    numbers=[1,4,3,3,5]
    assert quick_sort(numbers) == [1,3,3,4,5]