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
    def reversal(self,node):
        temp=Node()
        if node.next==None:
            self.head=node
            return
        self.reversal(node.next)
        temp=node.next
        temp.next=node
        node.next=None

def compare(l1,l2):
    while l1 and l2:
        if l1.data!=l2.data:
            print("Not Palindrome")
            return
        l1=l1.next
        l2=l2.next
    if l1==None and l2==None:
        print("Palindrome")
    
if __name__=='__main__':
    l1=LinkedList()
    n=int(input("How many values you want to insert? : "))
    for i in range(n):
        d=(input("Enter Data : "))
        l1.insert(d)
    l1.print()
    l2=copy.deepcopy(l1)
    l1.reversal(l1.head)
    compare(l1.head,l2.head)
    print("End")
        