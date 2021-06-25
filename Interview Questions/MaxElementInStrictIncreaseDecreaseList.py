def max(arr,l,h):
    mid=(l+h)//2
    if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
        print("Max : ",arr[mid])
        return
    elif arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]: #Elements at right are bigger
        max(arr[mid+1:h],mid+1,h)
    else:# arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]: #Elements at right are bigger
        max(arr[l:mid-1],l,mid-1)
 
 
if __name__=='__main__':
    l=[]
    n=int(input("How many values you want to insert? : "))
    for i in range(n):
        d=int(input())
        l.append(d)
    print("List : ",l)
    max(l,0,n)
    print("End")
        