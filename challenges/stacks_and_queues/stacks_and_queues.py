class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            wanted = self.top
            self.top = self.top.next
            wanted.next = None
            return wanted.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def peak(self):
        if self.top is None:
            raise AttributeError('The Stack is Empty')
        else:
            return self.top.value


test_stack = Stack()
test_stack.push('Apple')
test_stack.push('Cherry')
test_stack.push('Banana')
print(test_stack.peak())
test_stack.pop()
print(test_stack.peak())
test_stack.pop()
print(test_stack.peak())
test_stack.pop()
print(test_stack.is_empty())
