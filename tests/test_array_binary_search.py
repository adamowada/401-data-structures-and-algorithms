from challenges.array_binary_search.array_binary_search import array_binary_search

def test_binary_search_exists():
    test = array_binary_search([1,24,55], 24)
    assert test


def test_binary_search_odd():
    test = array_binary_search([1,24,55], 24)
    assert test == 1


def test_binary_search_odd2():
    test = array_binary_search([1,24,55], 24)
    assert test != 0 & test != 2


def test_binary_search_even():
    test = array_binary_search([1,24,55,66], 24)
    assert test == 1


def test_binary_search_even2():
    test = array_binary_search([1,24,55,66], 55)
    assert (test != 0 & test != 1) & test != 3
