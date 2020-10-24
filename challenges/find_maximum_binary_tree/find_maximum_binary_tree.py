class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_maximum_binary_tree(root):
    max = root.val
    q = [root]
    while q:
        temp = q.pop(0)
        if temp.val > max:
            max = temp.val
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return max
