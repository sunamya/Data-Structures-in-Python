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
        
def BFS(root):
    if root == None:
        return 
    queue=[]
    queue.append(root)
    while len(queue)>0:
        print(queue[0].data,end = " ")
        node=queue.pop(0)
        if node.left != None:
            queue.append(node.left)
        if node.right !=None:
            queue.append(node.right)
    
root=Node(1)

if __name__=='__main__':
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        insert(root,num)
    print("BFS Traversal : ")
    print(BFS(root))
    print("End")