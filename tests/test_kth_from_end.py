from challenges.ll_kth_from_end.ll_kth_from_end import Node, Linked_List
import pytest

def test_kth_value():
    test = Linked_List()
    test.head = Node(1)
    test.head.next = Node(2)
    test.head.next.next = Node(3)
    assert test.kth_from_end(2) == 1
    assert test.kth_from_end(1) == 2
    assert test.kth_from_end(0) == 3


def test_kth_value_exception():
    test = Linked_List()
    test.head = Node(1)
    test.head.next = Node(2)
    test.head.next.next = Node(3)
    with pytest.raises(Exception) as message:
        test.kth_from_end(4)
    assert '' in str(message.value)
