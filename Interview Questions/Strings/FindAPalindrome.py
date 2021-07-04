#User function Template for python3

class Solution:

    def countMin(self, Str):
        # code here
        if len(Str)==1 or len(Str)==0:
            return 0
        if len(Str)==2:
            if Str[0]==Str[1]:
                return 0
            else:
                return 1
        n=len(Str)
        table = [[0 for i in range(n)]
                for i in range(n)]
        l, h, gap = 0, 0, 0
     
        # Fill the table
        for gap in range(1, n):
            l = 0
            for h in range(gap, n):
                if Str[l] == Str[h]:
                    table[l][h] = table[l + 1][h - 1]
                else:
                    table[l][h] = (min(table[l][h - 1],
                                       table[l + 1][h]) + 1)
                l += 1
     
        return table[0][n - 1];

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends