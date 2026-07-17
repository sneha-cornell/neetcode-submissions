class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #unsorted array of nums (don't do sorting)
        #return kth largest element in value not freq.
        #use heap to do the sorting

        heap = []
        for n in nums: 
            heapq.heappush(heap,n)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
