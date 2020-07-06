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


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.front is None:
            self.front = Node(value)
            self.rear = self.front
        else:
            second = self.rear
            self.rear = Node(value)
            second.next = self.rear

    # logic leaves a self.rear
    def dequeue(self):
        if self.front:
            wanted = self.front
            self.front = self.front.next
            wanted.next = None
            return wanted.value

    def peek(self):
        if self.front is None:
            raise AttributeError('The Queue is Empty')
        else:
            return self.front.value

    def is_empty(self):
        return self.front == None


test_queue = Queue()
test_queue.enqueue('Adam')
test_queue.enqueue('Bill')
test_queue.enqueue('Charles')

print(test_queue.front.value)
print(test_queue.front.next.next.value)
test_queue.dequeue()
print(test_queue.front.value)
print(test_queue.front.next.value)
print(test_queue.is_empty())
test_queue.dequeue()
test_queue.dequeue()
print(test_queue.is_empty())



# test_stack = Stack()
# test_stack.push('Apple')
# test_stack.push('Cherry')
# test_stack.push('Banana')
# print(test_stack.peak())
# test_stack.pop()
# print(test_stack.peak())
# test_stack.pop()
# print(test_stack.peak())
# test_stack.pop()
# print(test_stack.is_empty())
