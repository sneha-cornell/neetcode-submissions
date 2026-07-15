class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input - string 
        #output - integer length of longest substring (contiguous)
        #handles duplicates using set 
        seen = {}
        l=0
        best =0

        for right, char in enumerate(s):
            if char in seen and seen[char]>=l:
                l = seen[char]+1
            seen[char]=right
            best = max(best,right-l+1)
        return best 
