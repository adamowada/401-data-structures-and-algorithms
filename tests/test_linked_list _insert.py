from challenges.linked_list.linked_list import Node, LinkedList

def test_node_exist():
    assert Node


def test_linked_list_exist():
    assert LinkedList


def test_linked_list_append():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.append(3)
    assert ll.head.next.next.value == 3
    assert ll.head.next.next.next == None


def test_linked_list_insert_before():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.insert_before(2, 3)
    assert ll.head.next.value == 3
    assert ll.head.next.next.value == 2


def test_linked_list_insert_after():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.insert_after(1, 4)
    assert ll.head.next.value == 4
    assert ll.head.next.next.value == 2