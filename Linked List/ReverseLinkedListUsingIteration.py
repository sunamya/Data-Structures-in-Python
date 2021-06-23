class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def printlist(self): #Print List
        temp=self.head
        print("List is : ")
        while temp:
            print(temp.data, end = " ")
            temp=temp.next
            
    def insertatbeg(self,num): #Insert at beginning
        node=Node(num)
        if self.head != None:
            node.next=self.head
            self.head=node
        else:
            self.head=node
    
    def reverse(self):
        prev=Node()
        temp=Node()
        current=self.head
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.head=prev

if __name__=='__main__':
    llist=LinkedList()
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        llist.insertatbeg(num)
        llist.printlist()
    print("\n Reversed List : ")
    llist.reverse()
    llist.printlist()
    print("\nEnd of Linked List")
