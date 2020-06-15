class Node:
    """
    This is the node class
    """

    def __init__(self, value, next_=None):
        """
        This is the initialization of the Node class
        """
        self.value = value
        self.next_ = next_


class LinkedList:
    """
    This is the linked_list class
    """

    def __init__(self):
        """
        This is the initialization of the linked_list
        """
        self.head = None

    def insert(self, value):
        """
        Inserts node into linked_list
        """
        node = Node(value)
        if self.head is not None:
            node.next_ = self.head
        self.head = node


linked_list = LinkedList()

linked_list.insert('Apple')
linked_list.insert('Orange')
linked_list.insert('Banana')
linked_list.insert('Pear')
linked_list.insert('Peach')

