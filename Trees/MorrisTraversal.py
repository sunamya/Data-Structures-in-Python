from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def MorrisTraversal(root):
    current=root
    while current:
        if current.left==None:
            print(current.data,end=" ")
            current=current.right
        else:
            pre=current.left
            while pre.right!=None and pre.right!=current:
                pre=pre.right
            if pre.right==None:
                pre.right=current
                current=current.left
            else:
                pre.right = None
                print(current.data,end=" ")
                current = current.right
    
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    MorrisTraversal(root)
    print("End")