class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None
        
class StackLinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,x): #Insertion at Beginning
        node=Node(x)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    
    def printstack(self):
        temp=self.head
        print("\nStack : ")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        
    def reverse(self):
        stk=[]
        temp=self.head
        while temp:
            stk.append(temp)
            temp=temp.next
        self.head=temp
        while len(stk)!=0:
            temp.next=stk.pop()
            temp=temp.next
        temp.next=None
        
if __name__=='__main__':
    stack=StackLinkedList()
    n=int(input("\nHow many elements you want to insert : "))
    for x in range(n):
        data=int(input("\nEnter data : "))
        stack.insert(data)
    stack.printstack()
    stack.reverse()
    stack.printstack()