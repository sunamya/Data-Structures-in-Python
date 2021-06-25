import copy
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

def compare(l1,l2,l3,num):
    while l1:
        b=l2
        c=l3
        while b and c:
            s=l1.data+b.data+c.data
            if s==num:
                print("Triplets found : ",l1.data," ",b.data," ",c.data)
                return True
            
            elif s<num:
                b=b.next
            else:
                c=c.next
            
        l1=l1.next
    print("No triplet found")
    
if __name__=='__main__':
    l1=LinkedList()
    l2=LinkedList()
    l3=LinkedList()
    n=int(input("How many values you want to insert? : "))
    for i in range(n):
        d=int(input("Enter Data : "))
        l1.insert(d)
    l1.print()
    for i in range(n):
        d=int(input("Enter Data : "))
        l2.insert(d)
    l2.print()
    for i in range(n):
        d=int(input("Enter Data : "))
        l3.insert(d)
    l3.print()
    n=int(input("Enter target sum : "))
    compare(l1.head,l2.head,l3.head,n)
    print("End")
        