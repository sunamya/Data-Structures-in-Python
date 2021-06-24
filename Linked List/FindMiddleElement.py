class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def add(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        node.next=self.head
        self.head=node
    
    def display(self):
        temp=self.head
        print("Queue : ")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
            
    def findmiddle(self):
        f1=self.head
        f2=self.head
        if self.head is not None:
            while (f1 is not None and f1.next is not None):
                f1=f1.next.next
                f2=f2.next
            print("The middle element is: ", f2.data)
                
        
if __name__=='__main__':
    l=LinkedList()
    n=int(input("How many values you want to insert? : "))
    for i in range(n):
        d=int(input("Enter Data : "))
        l.add(d)
    l.display()
    l.findmiddle()
    print("End")
        