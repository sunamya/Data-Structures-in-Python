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
            
def univsins(l1, l2):
    union=LinkedList()
    iint=LinkedList()
    temp=union
    t2=iint
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    c1=l1
    c2=l2
    u=[]
    i1=[]
    i2=[]
    while c1 and c2:
        if c1.data not in u:
            u.append(c1.data)
            i1.append(c1.data)
            union.next=c1
            union=c1
        if c1.data in i2:
            iint.next=c1
            iint=c1
        c1=c1.next
        if c2.data not in u:
            u.append(c2.data)
            i2.append(c2.data)
            union.next=c2
            union=c2
        if c2.data in i1:
            iint.next=c2
            iint=c2
        c2=c2.next
    while c1:
        if c1.data not in u:
            u.append(c1.data)
            union.next=c1
            union=c1
        c1=c1.next
    while c2:
        if c2.data not in u:
            u.append(c2.data)
            union.next=c2
            union=c2
        c2=c2.next
    print(i1," ",i2)
    union=temp.next
    iint=t2.next
    t2=None
    temp=None
    t=union
    print("UNION : ")
    while t:
        print(t.data,end=" ")
        t=t.next
    print("INTERSECTION : ")
    t=iint
    while t:
        print(t.data,end=" ")
        t=t.next
    
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
    univsins(l1.head,l2.head)
    print("End")
        