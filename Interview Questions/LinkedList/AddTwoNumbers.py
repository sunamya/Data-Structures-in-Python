#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        vis1={}
        vis2={}
        vis3={}
        cnt=1
        while first.next:
            vis1[cnt]=first
            cnt+=1
            first=first.next
        vis1[cnt]=first
        cnt=1
        while second.next:
            vis2[cnt]=second
            cnt+=1
            second=second.next
        vis2[cnt]=second
        l1=len(vis1)
        l2=len(vis2)
        carry=0
        if l1<l2:
            while l1>0:
                sum=(vis2[l2].data+vis1[l1].data+carry)%10
                carry=(vis2[l2].data+vis1[l1].data+carry)//10
                vis3[l2]=Node(sum)
                l1-=1
                l2-=1
            while l2>0:
                sum=(vis2[l2].data+carry)%10
                carry=(vis2[l2].data+carry)//10
                vis3[l2]=Node(sum)
                l2-=1
        elif l1>l2:
            while l2>0:
                sum=(vis2[l2].data+vis1[l1].data+carry)%10
                carry=(vis2[l2].data+vis1[l1].data+carry)//10
                vis3[l1]=Node(sum)
                l1-=1
                l2-=1
            while l1>0:
                sum=(vis1[l1].data+carry)%10
                carry=(vis1[l1].data+carry)//10
                vis3[l1]=Node(sum)
                l1-=1
        else:
            while l1>0 and l2>0:
                sum=(vis2[l2].data+vis1[l1].data+carry)%10
                carry=(vis2[l2].data+vis1[l1].data+carry)//10
                vis3[l1]=Node(sum)
                l1-=1
                l2-=1
        node=Node(None)
        cnt=1
        l3=len(vis3)
        start=node
        key=list(vis3.keys())
        while cnt<=l3:
            temp=Node(vis3[cnt].data)
            node.next=temp
            node=node.next
            cnt+=1
        if carry>0:
            node=Node(carry)
            node.next=start.next
            start.next=node
        return start.next
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends