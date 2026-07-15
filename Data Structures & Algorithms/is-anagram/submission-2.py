class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input - 2 strings
        #output - boolean
        #string with english letters only or unicode 
        #case sensitive?
        #whitespace/punctuation?

        return sorted(s)==sorted(t)