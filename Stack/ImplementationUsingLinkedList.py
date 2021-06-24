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
    
    def delete(self): #Deletion at Beginning
        if self.head==None:
            print("\nNo Elements")
        else:
            temp=self.head
            self.head=temp.next
            temp=None
    
    def printstack(self):
        temp=self.head
        print("\nStack : ")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
            
    def top(self):
        return self.head.data
        
if __name__=='__main__':
    stack=StackLinkedList()
    n=int(input("\nHow many elements you want to insert : "))
    for x in range(n):
        data=int(input("\nEnter data : "))
        stack.insert(data)
    stack.printstack()
    stack.delete()
    stack.delete()
    top=stack.top()
    print("\nTop : ",top)
    stack.delete()
    stack.printstack()