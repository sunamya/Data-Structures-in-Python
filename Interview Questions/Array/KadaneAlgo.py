#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,A,size):
        ##Your code here
        # stores the maximum sum sublist found so far
        max_so_far = A[0]
     
        # stores the maximum sum of sublist ending at the current position
        max_ending_here = A[0]
     
        # traverse the given list
        for i in range(1, size):
     
            # update the maximum sum of sublist "ending" at index `i` (by adding the
            # current element to maximum sum ending at previous index `i-1`)
            max_ending_here = max_ending_here + A[i]
     
            # maximum sum should be more than the current element
            max_ending_here = max(max_ending_here, A[i])
     
            # update the result if the current sublist sum is found to be greater
            max_so_far = max(max_so_far, max_ending_here)
     
        return max_so_far


import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends