class Stack:
    def __init__(self):
        self.stack=[]
    
    def add(self,x):
        self.stack.append(x)
        
    def check_empty(self):
        if len(self.stack)==0:
            return True
        return False
    
    def delete(self):
        if (self.check_empty()):
            print("\nStack is empty")
        else:
            self.stack.pop()
            self.printstack()
    
    def printstack(self):
        print("\nStack : ")
        for x in self.stack:
            print(x,end=" ")
    
    def top(self):
        return self.stack[-1]
    
if __name__=='__main__':
    stack=Stack()
    n=int(input("\nHow many elements you want to insert : "))
    print(stack.check_empty())
    for x in range(n):
        data=int(input("\nEnter data : "))
        stack.add(data)
    stack.printstack()
    stack.delete()
    top=stack.top()
    print("\nTop : ",top)
    stack.delete()
    stack.delete()