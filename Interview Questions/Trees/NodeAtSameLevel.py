from collections import deque

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def findRightNode(root):
    if root is None:
        return None
 
    queue = deque()
    queue.append(root)
    i=1
    while queue:
        print("LEVEL : ",i)
        size = len(queue)
        while size > 0:
            size = size - 1
            front = queue.popleft()
            print(front.data,end=" ")
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
        i+=1
    return None
 
 
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    findRightNode(root)

