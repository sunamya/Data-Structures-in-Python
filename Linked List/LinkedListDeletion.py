class Node:
    def __init__(self,data):
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
    
    def deleteatbeg(self): #Delete at beginning
        temp=self.head
        self.head=temp.next
        temp=None
    
    def deleteatn(self,n): #Delete at nth pos
        temp=self.head
        if temp.next != None:
            if temp.data==n:
                self.head=temp.next
                temp=None
                return
        while temp:
            if temp.data==n:
                break
            prev=temp
            temp=temp.next
        if temp.next!=None:
            prev.next=temp.next
        temp=None
            
        
if __name__=='__main__':
    llist=LinkedList()
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        llist.insertatbeg(num)
        llist.printlist()
    print("\nDelete at nth position")
    llist.deleteatbeg()
    llist.printlist()
    newn=int(input("\nEnter Number to be deleted: "))
    llist.deleteatn(newn)
    llist.printlist()
    print("\nEnd of Linked List")
