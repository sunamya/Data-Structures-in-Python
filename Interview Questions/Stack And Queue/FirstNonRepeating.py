#User function Template for python3
from queue import Queue
MAX_CHAR = 26
class Solution:
	def FirstNonRepeating(self, Str):
		global MAX_CHAR
        q = Queue()
        charCount = [0] * MAX_CHAR
        res=[]
        for i in range(len(Str)):
     
            q.put(Str[i])
     
            charCount[ord(Str[i]) - ord('a')] += 1
     
            while (not q.empty()):
                if (charCount[ord(q.queue[0]) - ord('a')] > 1):
                    q.get()
                else:
                    res.append(q.queue[0])
                    break
     
            if (q.empty()):
                res.append("#")
        return "".join(res)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends