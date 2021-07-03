#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		i=1
		S=list(S)
		N=[]
		for x in S:
		    if x not in N:
		        N.append(x)
		return "".join(N)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends