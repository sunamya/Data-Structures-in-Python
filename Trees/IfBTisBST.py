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
        
def isBSTUtil(root, prev):
    if (root != None):
        if (isBSTUtil(root.left, prev) == True):
            return False

        if (prev != None and
            root.data <= prev.data):
            return False
 
        prev = root
        return isBSTUtil(root.right, prev)
     
    return True
 
def isBST(root):
    prev = None
    return isBSTUtil(root, prev)
    
root=Node(1)

if __name__=='__main__':
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        insert(root,num)
    if (isBST(root) == None):
        print("Is BST")
    else:
        print("Not a BST")
    print("End")