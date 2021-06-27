def RotatedArraySearch(arr,x):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        print(start," ",mid," ",end)
        if arr[mid]==x:
            return mid
        elif arr[mid]<=arr[end]:
            if x>arr[mid] and x<=arr[end]:
                start=mid+1
            else:
                end=mid-1
        else:
            if arr[start]<=x and x<arr[mid]:
                end=mid-1
            else:
                start=mid+1
    return -1
    
if __name__=='__main__':
    arr=[]
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        arr.append(num)
    x=int(input("Enter number to be searched : "))
    rot=RotatedArraySearch(arr,x)
    print(rot)
    if rot>=0:
        print("Found at ",rot)
    else:
        print("Not Found")
    print("End")
    