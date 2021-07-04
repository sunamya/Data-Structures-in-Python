class Solution:
    def find_permutation(self, S):
        # Code here
        if S=="":
            return ([0])
        ans=[]
        self.permute(S,"",ans)
        return sorted(ans)
    def permute(self,s, answer,d):
        if (len(s) == 0):
            print(answer, end = "  ")
            return
         
        for i in range(len(s)):
            ch = s[i]
            left_substr = s[0:i]
            right_substr = s[i + 1:]
            rest = left_substr + right_substr
            print(rest," ",answer + ch)
            self.permute(rest, answer + ch,d)