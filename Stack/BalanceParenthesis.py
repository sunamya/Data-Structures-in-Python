def check(s):
    stk=[]
    l=len(s)
    for i in range(l):
        if s[i]=='{' or s[i]=='(' or s[i]=='[':
            stk.append(s[i])
        elif s[i]=='}' or s[i]==')' or s[i]==']':
            if len(stk)>0:
                stk.pop()
            else:
                print("Not balanced")
                return
    if stk!=[]:
        print("Not balanced")
    else:
        print("Balanced")
                
if __name__=='__main__':
    s=input("\nEnter String : ")
    check(s)