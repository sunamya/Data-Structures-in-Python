def BinarySearch(arr,x):
    s=0
    n=len(arr)
    while s<=n:
        mid=(s+n)//2
        if arr[mid-1]==x:
            return mid
        elif x<arr[mid-1]:
            n=mid-1
        elif x>arr[mid-1]:
            s=mid+1
    return -1

if __name__=='__main__':
    arr=[]
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        arr.append(num)
    x=int(input("Enter number to be searched : "))
    pos=BinarySearch(arr,x)
    if (pos):
        print("Found at ",pos)
    else:
        print("Not found")