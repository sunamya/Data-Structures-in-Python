class Queue:
    def __init__(self):
        self.queue=[]
        
    def Enqueue(self,data):
        self.queue.append(data)
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Can not delete")
            return
        self.queue.pop(0)
        
    def isEmpty(self):
        return self.queue==[]
    
    def size(self):
        return len(self.queue)
        
    def display(self):
        print("Queue : ",self.queue)

if __name__=='__main__':
    queue=Queue()
    n=int(input("\nHow many elements do you want to enter : "))
    queue.isEmpty()
    for i in range(n):
        d=int(input("\nEnter data : "))
        queue.Enqueue(d)
    print(queue.isEmpty())
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.display()
    