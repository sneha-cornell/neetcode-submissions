class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.expand(s,i,i)
            even = self.expand(s,i,i+1)
            if len(odd)>len(res):
                res = odd
            if len(even)>len(res):
                res=even
        return res

    def expand(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]