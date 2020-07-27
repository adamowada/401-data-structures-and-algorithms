class Node:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def pre_order(self, start, bucket):
        if start:
            bucket.append(start.value)
            # bucket = bucket.append(self.pre_order(start.left_child, bucket))
            # bucket = bucket.append(self.pre_order(start.right_child, bucket))
            if start.left_child:
                bucket.append(self.pre_order(start.left_child, bucket))
            if start.right_child:
                bucket.append(self.pre_order(start.right_child, bucket))
        return bucket

    def in_order(self):
        pass

    def post_order(self):
        pass


tree = BinaryTree('A')
tree.root.left_child = Node('B')
tree.root.right_child = Node('C')
tree.root.left_child.left_child = Node('D')
tree.root.left_child.right_child = Node('E')
tree.root.right_child.left_child = Node('F')
tree.root.right_child.right_child = Node('G')

print(tree.pre_order(tree.root, []))
