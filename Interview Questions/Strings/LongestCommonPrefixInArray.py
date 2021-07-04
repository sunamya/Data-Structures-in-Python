#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        prefix=arr[0]
        for i in range(1,n):
            prefix=self.Prefix(prefix,arr[i])
        return prefix if prefix !="" else -1
    def Prefix(self,str1,str2):
        result = "";
        n1 = len(str1)
        n2 = len(str2)
        i = 0
        j = 0
        while i <= n1 - 1 and j <= n2 - 1:
            if (str1[i] != str2[j]):
                break
            result += str1[i]
            i += 1
            j += 1
        return (result)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends