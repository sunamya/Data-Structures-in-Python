class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def topView(root):
    #Write your code here
    dict={}
    Top(root,0,0,dict)
    for key in sorted(dict.keys()):
        print(dict.get(key)[0], end=' ')

def Top(root,dis,level,dict):
    if root==None:
        return
    if dis not in dict or level<dict[dis][1]:
        dict[dis] = (root.info, level)
    Top(root.left, dis - 1, level + 1, dict)
    Top(root.right, dis + 1, level + 1, dict)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)