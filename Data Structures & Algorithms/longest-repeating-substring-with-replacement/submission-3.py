class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #input - s(uppercase english letters), k(integer)
        #output - length integer 
        #at most k char changes or exactly k - at most 
        #replace with any letter or only those existing in string 

        #window length - max count of char in s <=k

        count = [0]*26
        l = 0
        for right in range(len(s)):
            count[ord(s[right])-ord('A')]+=1
            if (right-l+1)-max(count)>k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
        return len(s)-l

