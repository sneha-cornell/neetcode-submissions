class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input - 2 strings
        #output - boolean
        #string with english letters only or unicode 
        #case sensitive?
        #whitespace/punctuation?

        # return sorted(s)==sorted(t)
        if len(s)!=len(t):
            return False
        count = [0]*26
        for cs, ct in zip(s,t):
            count[ord(cs)-ord('a')]+=1
            count[ord(ct)-ord('a')]-=1
        return all(c==0 for c in count)