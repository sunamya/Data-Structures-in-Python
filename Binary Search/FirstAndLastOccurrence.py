def BinarySearchMin(arr,x):
    s=0
    n=len(arr)
    res=-1
    while s<=n:
        mid=(s+n)//2
        if x==arr[mid]:
            res=mid
            n=mid-1
        elif x<arr[mid]:
            n=mid-1
        else:
            s=mid+1
    return res+1
    
def BinarySearchMax(arr,x):
    s=0
    n=len(arr)
    res=-1
    while s<=n:
        mid=(s+n)//2
        if x==arr[mid-1]:
            res=mid
            s=mid+1
        elif x<arr[mid-1]:
            n=mid-1
        else:
            s=mid+1
    return res

if __name__=='__main__':
    arr=[]
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        arr.append(num)
    x=int(input("Enter number to be searched : "))
    pos=BinarySearchMin(arr,x)
    print(pos)
    if pos>0:
        print("Min Found at ",pos)
    else:
        print("Min Not found")
    pos=BinarySearchMax(arr,x)
    if pos>0:
        print("Max Found at ",pos)
    else:
        print("Max Not found")