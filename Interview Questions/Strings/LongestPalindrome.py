#User function Template for python3

class Solution:
    def longestPalin(self, S):
        # code here
        start=0
        l=len(S)
        low=0
        high=0
        maxlength=1
        for i in range(1,l):
            #Even Length
            low=i-1
            high=i
            while low>=0 and high<l and S[low]==S[high]:
                if high-low+1>maxlength:
                    start=low
                    maxlength=high-low+1
                low-=1
                high+=1
            #Odd Length
            low=i-1
            high=i+1
            while low>=0 and high<l and S[low]==S[high]:
                if high-low+1>maxlength:
                    start=low
                    maxlength=high-low+1
                low-=1
                high+=1
        return S[start:start+maxlength]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends