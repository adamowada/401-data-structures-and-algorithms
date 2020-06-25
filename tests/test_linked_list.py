from challenges.linked_list.linked_list import Node, LinkedList

def test_node_exist():
    assert Node


def test_linked_list_exist():
    assert LinkedList


def test_empty_linked_list():
    test = LinkedList()
    assert test


def test_ll_insert():
    test = LinkedList()
    test.insert('Apple')
    assert test.includes('Apple')


def test_ll_head():
    test = LinkedList()
    test.insert('Apple')
    assert test.head.value == 'Apple'


def test_ll_insert_multiple():
    test = LinkedList()
    test.insert('Apple')
    test.insert('Cherry')
    assert test.includes('Apple')
    assert test.includes('Cherry')


def test_ll_includes_true():
    test = LinkedList()
    test.insert('Apple')
    assert test.includes('Apple')


def test_ll_includes_false():
    test = LinkedList()
    test.insert('Apple')
    expected = False
    actual = test.includes('Banana')
    assert actual == expected


def test_ll_return_collection_of_values():
    test = LinkedList()
    test.insert('Apple')
    test.insert('Cherry')
    assert str(test) == "{'Cherry'}->{'Apple'}->None"
