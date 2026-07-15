class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input- array of integers (can be neg?, can there
        # be duplicates,empty array)
        #output - integer of length of longest sequence 
        #brute force is sort but not O(n) time 
        num_set = set(nums)
        longest =0

        for num in num_set: 
            if num-1 not in num_set: 
                curr= num
                length = 1
                while curr+1 in num_set: 
                    curr+=1
                    length+=1
                longest = max(longest,length)
        return longest

