from challenges.insertion_sort.insertion_sort import insertion_sort

def test_function_exists():
    assert insertion_sort


def test_already_sorted():
    array = [1,2,3,4,5]
    test = insertion_sort(array)
    assert test == [1,2,3,4,5]


def test_insertion_sort():
    array = [5,4,3,2,1]
    test = insertion_sort(array)
    assert test == [1,2,3,4,5]


def test_insertion_sort_duplicates():
    array = [1,5,4,3,2,1]
    test = insertion_sort(array)
    assert test == [1,1,2,3,4,5]


def test_insertion_sort_single():
    array = [1]
    test = insertion_sort(array)
    assert test == [1]


def test_insertion_sort_empty():
    array = []
    test = insertion_sort(array)
    assert test == []
