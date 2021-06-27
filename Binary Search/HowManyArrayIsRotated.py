def BinarySearchArrayRotated(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        next=(mid+1)%end
        prev=(mid+end-1)%end
        if arr[start]<=arr[end]:
            return start
        elif arr[mid]<=arr[next] and arr[mid]<=arr[prev]:
            return mid
        elif arr[mid]<=arr[end]:
            end=mid-1
        elif arr[mid]>=arr[start]:
            start=mid+1
    return -1
    
if __name__=='__main__':
    arr=[]
    ip=int(input("How many numbers you want to enter : "))
    for i in range(ip):
        num=int(input("\nEnter data : "))
        arr.append(num)
    rot=BinarySearchArrayRotated(arr)
    if rot>0:
        print("Rotated by ",rot)
    print("End")
    