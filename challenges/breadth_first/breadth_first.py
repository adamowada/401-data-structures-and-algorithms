class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def breadth_first(root):
    order = []
    q = [root]
    while q:
        temp = q.pop(0)
        order.append(temp.val)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return order

