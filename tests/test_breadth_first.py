from challenges.breadth_first.breadth_first import Node, breadth_first

def test_node_and_breadth_fist_exist():
    assert Node
    assert breadth_first


def test_one_node():
    test = Node(9)
    assert breadth_first(test) == [9]


def test_unbalanced_tree():
    test = Node(9)
    test.left = Node(0)
    test.left.left = Node(1)
    test.left.left.left = Node(4)
    assert breadth_first(test) == [9,0,1,4]

def test_full_tree():
    test = Node(1)
    test.left = Node(2)
    test.right = Node(3)
    test.left.left = Node(4)
    test.left.right = Node(5)
    test.right.left = Node(6)
    test.right.right = Node(7)
    assert breadth_first(test) == [1,2,3,4,5,6,7]
