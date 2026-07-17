class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #is nums sorted 
        #return k most frequent in array 

        #keys- values, vals- freq 
        count =Counter(nums)
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq,num in heap]

