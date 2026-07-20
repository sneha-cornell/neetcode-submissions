class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #O(n^2*k) - k is average word length 
        #dp state dp[i] is if s[:i] can be broken down into words
        word_set = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0]= True #empty prefix is trivially breakable

        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set: #tests if s[:j] is breakable and s[j:i] is a word in dict, then s[:i] works
                    dp[i]=True 
                    break #done once we find any valid split for dp[:i]
        return dp[n]
