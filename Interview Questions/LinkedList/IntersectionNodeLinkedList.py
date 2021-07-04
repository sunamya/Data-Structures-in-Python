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

def intersectionnode(l1,l2):
    a, b = l1, l2
    while (a != b):
        a = l2 if not a else a.next
        b = l1 if not b else b.next
    return a
    
if __name__=='__main__':
    l1=LinkedList()
    l2=LinkedList()
    l3=LinkedList()
    n=int(input("How many values you want to insert? : "))
    for i in range(n):
        d=int(input("Enter Data : "))
        l1.insert(d)
    l1.print()
    n=int(input("How many values you want to insert? : "))
    for i in range(n):
        d=int(input("Enter Data : "))
        l2.insert(d)
    l2.print()
    a=intersectionnode(l1.head,l2.head)
    print("End",a)
        