#User function Template for python3

class Solution:

    def longestSubstrDitinctChars(self, string):
        seen = {}
        maximum_length = 0
        start = 0
          
        for end in range(len(string)):
            if string[end] in seen:
                start = max(start, seen[string[end]] + 1)
            seen[string[end]] = end
            maximum_length = max(maximum_length, end-start + 1)
        return maximum_length

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDitinctChars(S)

        print(ans)

# } Driver Code Ends