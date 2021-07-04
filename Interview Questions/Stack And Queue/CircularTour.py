'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,arr, n):
        start = 0 
        end = 1 
        curr_petrol = arr[start][0] - arr[start][1] 
        while(end != start or curr_petrol < 0 ): 
            while(curr_petrol < 0 and start != end): 
                curr_petrol -= arr[start][0] - arr[start][1]
                start = (start +1)%n 
                if start == 0: 
                    return -1
            curr_petrol += arr[end][0] - arr[end][1] 
            end = (end +1) % n 
        return start

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends