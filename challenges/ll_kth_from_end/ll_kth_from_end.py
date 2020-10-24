class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def kth_from_end(self, k):
        counter = self.head
        current = self.head
        while current.next:
            if k <= 0:
                counter = counter.next
            else:
                k -= 1
            current = current.next
        if k > 0:
            raise Exception
        else:
            return counter.val
