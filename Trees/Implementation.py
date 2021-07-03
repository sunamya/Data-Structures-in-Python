from collections import deque

class Node:
    def __init__(self,data=0):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    node=Node(data)
    if root==None:
        root=node
    elif data>root.data:
        if root.right == None:
            root.right = node
        else:
            insert(root.right,data)
    else:
        if root.left is None:
            root.left = node
        else:
           insert(root.left,data)

def inorderIterative(root):
    stack = deque()
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data, end=' ')
            curr = curr.right
        
def insearch(root):
    if root==None:
        return
    insearch(root.left)
    print(root.data,end=" ")
    insearch(root.right)

def preorderIterative(root):
 
    if root is None:
        return
    stack = deque()
    stack.append(root)

    while stack:
 
        curr = stack.pop()
 
        print(curr.data, end=' ')
        if curr.right:
            stack.append(curr.right)
 
        if curr.left:
            stack.append(curr.left)

def presearch(root):
    if root==None:
        return
    print(root.data,end=" ")
    presearch(root.left)
    presearch(root.right)
    
root=Node()

if __name__=='__main__':
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        insert(root,num)
    print("Inorder Traversal : ")
    insearch(root)
    print("Preorder Traversal : ")
    presearch(root)
    print("End")