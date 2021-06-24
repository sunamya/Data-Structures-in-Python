class Stack:
    def __init__(self):
        self.stack=[]
    
    def add(self,x):
        self.stack.append(x)
    
    def delete(self):
        return self.stack.pop()
        
def reverse(string):
    l=len(string)
    stack=Stack()
    for i in range(l):
        stack.add(string[i])
    new_string=""
    for i in range(l):
        new_string+=stack.delete()
    return new_string
    
    
if __name__=='__main__':
    n=input("\nEnter String : ")
    ns=reverse(n)
    print("\nNew String : ",ns)