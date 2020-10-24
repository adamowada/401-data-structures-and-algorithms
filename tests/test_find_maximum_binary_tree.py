from challenges.find_maximum_binary_tree.find_maximum_binary_tree import Node, find_maximum_binary_tree

def test_node_class_exists():
    assert Node


def test_find_maximum_binary_tree_function_exists():
    assert find_maximum_binary_tree


def test_works_with_one_node():
    test = Node(9)
    assert find_maximum_binary_tree(test) == 9


def test_works_with_tie():
    test = Node(9)
    test.left = Node(9)
    test.right = Node(7)
    assert find_maximum_binary_tree(test) == 9


def test_works_with_uniques_and_negatives():
    test = Node(10)
    test.left = Node(40)
    test.right = Node(22)
    test.left.left = Node(1)
    test.left.right = Node(0)
    test.right.left = Node(-1)
    test.right.right = Node(13)
    assert find_maximum_binary_tree(test) == 40


def test_unbalanced_tree():
    test = Node(9)
    test.left = Node(4)
    test.left.left = Node(3)
    test.left.left.left = Node(98)
    test.left.left.left.left = Node(0)
    test.left.left.left.left.left = Node(-77)
    assert find_maximum_binary_tree(test) == 98

