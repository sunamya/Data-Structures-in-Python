def BinarySearch(arr,s,n,x):
    mid=(s+n)//2
    print(mid," ",s," ",n)
    if s>n:
        return -1
    if arr[mid-1]==x:
        return mid
    elif x<arr[mid-1]:
        return BinarySearch(arr,0,mid-1,x)
    elif x>arr[mid-1]:
        return BinarySearch(arr,mid+1,n,x)
    else:
        return -1

if __name__=='__main__':
    arr=[]
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        arr.append(num)
    x=int(input("Enter number to be searched : "))
    pos=BinarySearch(arr,0,len(arr),x)
    if pos>0:
        print("Found at ",pos)
    else:
        print("Not found")