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
        
def findmin(root):
    if root == None:
        print("Empty")
        return
    elif root.left==None:
        return root.data
    return findmin(root.left)
    
def findmax(root):
    if root == None:
        print("Empty")
        return
    elif root.right==None:
        return root.data
    return findmin(root.right)
    
root=Node(10)

if __name__=='__main__':
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        insert(root,num)
    print("Min Element : ")
    print(findmin(root))
    print("Max Element : ")
    print(findmax(root))
    print("End")