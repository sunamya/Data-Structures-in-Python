
#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        if len(a)!=len(b):
            return 0
        x=len(a)
        va={}
        vb={}
        for i in range(x):
            if a[i] not in va.keys():
                va[a[i]]=1
            else:
                va[a[i]]+=1
            if b[i] not in vb.keys():
                vb[b[i]]=1
            else:
                vb[b[i]]+=1
        if va==vb:
            return 1
        else:
            return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends