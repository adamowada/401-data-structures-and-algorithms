class Node:
    """
    This is the Node class
    """

    def __init__(self, value, next=None):
        """
        This is the initialization of the Node class
        """
        self.value = value
        self.next = next


class LinkedList:
    """
    This is the LinkedList class
    """

    def __init__(self):
        """
        This is the initialization of the linked list
        """
        self.head = None

    def insert(self, value):
        """
        Inserts node into the beginning of the linked list (not append)
        """
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        """
        Returns true if node with value is in linked list. Otherwise returns false
        """
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        
        return False

    def __str__(self):
        string = ""
        current_node = self.head

        while current_node:
            string += (f"{ {current_node.value} }->")
            current_node = current_node.next
        
        string += "None"
        return string

    def append(self, value):
        """
        Inserts node at the end of the linked list (not insert)
        """
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = node

    def insert_before(self, target_value, value):
        """
        Inserts value node before target_value node
        """
        node = Node(value)

        current_node = self.head

        if current_node.value == target_value:
            self.insert(value)
            return

        while current_node.next.value is not target_value:
            current_node = current_node.next
            if current_node.next == None:
                print("Error not in linked list")
                return

        node.next = current_node.next
        current_node.next = node

    def insert_after(self, target_value, value):
        """
        Inserts value node after target_value node
        """
        node = Node(value)

        current_node = self.head

        while current_node.value is not target_value:
            current_node = current_node.next
            if current_node == None:
                print("Error not in linked list")
                return

        node.next = current_node.next
        current_node.next = node


linked_list = LinkedList()
linked_list.append('Apple')
linked_list.append('Banana')
linked_list.append('Cherry')
linked_list.insert_after('Cher0ry', 'Brock')
# linked_list.insert('Orange')
# linked_list.insert('Banana')
# linked_list.insert('Pear')
# linked_list.insert('Peach')
# print("linked_list includes 'Peach': ", linked_list.includes('Peach'))
print(str(linked_list))
