from collections import deque

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
def printVertical(root):
    if root is None:
        return
    dict = {}
    q = deque()
    q.append((root, 0))
    while q:
        node, dist = q.popleft()
        dict.setdefault(dist, []).append(node.key)
        if node.left:
            q.append((node.left, dist - 1))
        if node.right:
            q.append((node.right, dist + 1))
    for key in sorted(dict.keys()):
        print(dict.get(key))
 
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.left.right.left = Node(9)
    root.right.left.right.right = Node(10)
 
    printVertical(root)