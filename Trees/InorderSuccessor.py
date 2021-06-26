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
        
def insearch(root):
    if root==None:
        return
    insearch(root.left)
    print(root.data,end=" ")
    insearch(root.right)

def presearch(root):
    if root==None:
        return
    print(root.data,end=" ")
    presearch(root.left)
    presearch(root.right)

def delete(root,data):
    if root==None:
        return root
        
    if data<root.data:
        root.left=delete(root.left,data)
        return root
    elif data>root.data:
        root.right=delete(root.right,data)
        return root
    else:
        if (root.left == None and root.right==None): #No child node
            return None
        elif (root.left == None): #Right Child
            temp=root.right
            root=None
            return temp
        elif root.right==None: #Left Child
            temp=root.left
            root=None
            return temp
        else: #Both Childs
            sp=root
            s=root.right
            while s.left:
                sp=s
                s=s.left
            if sp!=root:
                sp.left=s.right
            else:
                sp.right=s.right
            root.key=s.key
        return root
            
def inOrderSuccessor(root, n):

    if n.right is not None:
        return minValue(n.right)

    succ=Node(None)
     
     
    while( root):
        if(root.data<n.data):
            root=root.right
        elif(root.data>n.data):
            succ=root
            root=root.left
        else:
            break
    return succ

def minValue(node):
    current = node
    while(current is not None):
        if current.left is None:
            break
        current = current.left
 
    return current

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
    temp = root.left
    succ = inOrderSuccessor( root, temp)
    if succ is not None:
        print("Inorder Successor of" ,
        temp.data ,"is" ,succ.data)
    else:
        print("InInorder Successor doesn't exist")
    insearch(root)
    print("End")