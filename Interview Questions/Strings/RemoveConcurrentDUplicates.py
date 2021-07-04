#User function Template for python3

class Solution:
    def remove (self, S):
		#code here
		start=0
		end=0
		S=list(S)
		l=len(S)
		N=list()
		x=1
		while x<l:
		    if S[x]!=S[x-1]:
		        N.append(S[x-1])
		        end+=1
		    else:
                while x < len(S) and S[x - 1] == S[x]:
                    x+=1
		    x+=1
		N.append(S[x-1])
	    N="".join(N)
	    end+=1
	    if end!=l:
	        self.remove(N)
	    return N
		            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.remove(S))


# } Driver Code Ends