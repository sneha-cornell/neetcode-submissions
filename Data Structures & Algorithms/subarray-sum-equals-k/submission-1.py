class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #input array nums can contain negative and positive integers 
        #so we can't use sliding window - need prefix sum + hash (window can shrink/become bigger unpredictably)
        seen = defaultdict(int)
        seen[0]=1
        running_sum =0
        count = 0

        for num in nums: 
            running_sum+=num
            count +=seen[running_sum-k]
            seen[running_sum]+=1
        return count