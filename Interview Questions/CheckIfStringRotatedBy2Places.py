#User function Template for python3



#Function to check if a string can be obtained by rotating
#another string by exactly 2 places.
class Solution():
    def isRotated(self,str1,str2):
        #code here
        if (len(str1) != len(str2)):
            return False
        if(len(str1) < 2):
            return str1 == str2
        l = len(str2)
        # Initialize string as anti-clockwise rotation
        anticlock_rot = str2[l - 2:] +str2[0: l - 2]
         
        # Initialize string as clock wise rotation
        clock_rot = str2[2:] + str2[0:2]
        # check if any of them is equal to string1
        return (str1 == clock_rot or
                str1 == anticlock_rot)
        
    

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
        s=str(input())
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends