class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(Node(child))


def fizzbuzz_tree(root):
    if root:
        print(fizzbuzz(root.value))
        if root.children:
            for i in root.children:
                fizzbuzz_tree(i)


def fizzbuzz(number):
    if number % 15 == 0:
        return 'fizzbuzz'
    if number % 5 == 0:
        return 'buzz'
    if number % 3 == 0:
        return 'fizz'
    return str(number)


root = Node(1)
root.add_child(2)
root.add_child(3)
root.add_child(4)
root.add_child(5)
root.children[0].add_child(6)
root.children[1].add_child(7)
root.children[2].add_child(8)
root.children[3].add_child(15)

fizzbuzz_tree(root)
