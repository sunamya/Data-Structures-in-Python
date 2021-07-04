#User function Template for python3


val={"I" :1,
"V" :5,
"X" :10,
"L" :50,
"C" :100,
"D" :500,
"M" :1000}
def romanToDecimal(s):
    # code here
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    s=list(s)
    sum=0
    for x in s:
        sum+=val[x]
    return sum

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        print(romanToDecimal(str(input())))
# } Driver Code Ends