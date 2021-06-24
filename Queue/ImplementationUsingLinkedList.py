class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None
        
class Queue:
    def __init__(self):
        self.front=self.rear=None
        
    def Enqueue(self,data):
        node=Node(data)
        if self.rear==None:
            self.front=self.rear=node
            return
        self.rear.next=node
        self.rear=node
    
    def Dequeue(self):
        if self.front==None:
            print("No element")
            return
        temp=self.front
        self.front=temp.next
        if(self.front == None):
            self.rear = None
    
    def isEmpty(self):
        if self.front==None:
            return True
        else:
            return False
    
    def display(self):
        temp=self.front
        print("Queue : ")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        
if __name__=='__main__':
    queue=Queue()
    print(queue.isEmpty())
    n=int(input("How many values you want to insert? : "))
    for i in range(n):
        d=int(input("Enter Data : "))
        queue.Enqueue(d)
    print(queue.isEmpty())
    queue.display()
    queue.Dequeue()
    queue.Dequeue()
    queue.Dequeue()
    queue.display()
    print("End")
        