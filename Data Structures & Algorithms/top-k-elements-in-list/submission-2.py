class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = {}
        
        # for num in nums: 
        #     freq[num]=freq.get(num,0)+1
        # sorted_keys = sorted(freq, key=lambda x:freq[x],reverse=True)
        # return sorted_keys[:k]

        freq = {}
        for num in nums: 
            freq[num]=freq.get(num,0)+1

        buckets=[[] for _ in range(len(nums)+1)]
        for num,count in freq.items():
            buckets[count].append(num)
        result=[]
        for i in range(len(buckets)-1,0,-1):
            result.extend(buckets[i])
            if len(result)>=k:
                return result[:k]
