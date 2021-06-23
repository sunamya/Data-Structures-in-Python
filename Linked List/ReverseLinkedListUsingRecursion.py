class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def printlist(self,node): #Print List
        if node==None:
            return
        print(node.data,end=" ")
        self.printlist(node.next)
        
    def recrev(self,node): #Print Reverse List
        temp=Node()
        if node.next==None:
            self.head=node
            return
        self.recrev(node.next)
        temp=node.next
        temp.next=node
        node.next=None
            
    def insertatbeg(self,num): #Insert at beginning
        node=Node(num)
        if self.head != None:
            node.next=self.head
            self.head=node
        else:
            self.head=node
    
    

if __name__=='__main__':
    llist=LinkedList()
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        llist.insertatbeg(num)
        #llist.printlist()
    print("\nList : ")
    llist.printlist(llist.head)
    llist.recrev(llist.head)
    print("\nReverse List : ")
    llist.printlist(llist.head)
    print("\nEnd of Linked List")
