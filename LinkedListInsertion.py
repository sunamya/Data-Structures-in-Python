class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    
    def printlist(self): #Print List
        temp=self.head
        print("\nList is : ")
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
            
    def insertatbeg(self,num): #Insert at beginning
        node=Node(num)
        if self.head != None:
            self.head.prev=node
            node.next=self.head
            self.head=node
        else:
            self.head=node
    
    def insertatn(self,num,n):
        node=Node(num)
        temp=self.head
        i=0
        if n==1:
            self.head.prev=node
            node.next=self.head
            self.head=node
        else:
            while temp and i<n-2:
                temp=temp.next
                i+=1
            if temp==None:
                print("Location doesn`t exist")
            else:
                node.next=temp.next
                node.prev=temp.next.prev
                temp.next=node
                temp.next.prev=node
            
    
    def reverseprint(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        print("\nReverse : ")
        while temp:
            print(temp.data,end=" ")
            temp=temp.prev
    
    

if __name__=='__main__':
    llist=DoubleLinkedList()
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        llist.insertatbeg(num)
        #llist.printlist()
    llist.printlist()
    llist.reverseprint()
    newn=int(input("Enter Number : "))
    l=int(input("Enter location where you want to insert : "))
    llist.insertatn(newn,l)
    llist.printlist()
    print("\nEnd of Linked List")