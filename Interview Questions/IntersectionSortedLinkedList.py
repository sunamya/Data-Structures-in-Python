class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    
    def print(self):
        temp=self.head
        print("List : ")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
            
def sortedIntersection(l1,l2):
    head=None
    if l1 is None:
        print("List 1 is empty")
        return
    elif l2 is None:
        print("List 2 is empty")
        return
    while l1 and l2:
        if l1.data==l2.data:
            res=Node(l1.data)
            if head==None:
                head=res
            else:
                res.next=head
                head=res
            l1=l1.next
            l2=l2.next
        elif l1.data<l2.data:
            l1=l1.next
        else:
            l2=l2.next
    print("Sorted List : ")
    while head:
        print(head.data,end=" ")
        head=head.next
        
    
if __name__=='__main__':
    l1=LinkedList()
    n=int(input("How many values you want to insert? : "))
    for i in range(n):
        d=int(input("Enter Data : "))
        l1.insert(d)
    l1.print()
    l2=LinkedList()
    n=int(input("How many values you want to insert? : "))
    for i in range(n):
        d=int(input("Enter Data : "))
        l2.insert(d)
    l2.print()
    sortedIntersection(l1.head,l2.head)
    print("End")
        