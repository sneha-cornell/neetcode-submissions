class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #max heap still holds stale values until they bubble to the top
        #so use deque that can discard stale elements from both ends
        dq= deque()
        result = []

        for i,n in enumerate(nums):
            #drop indices that fell out of window of left boundary 
            #dq stores values in decreasing order , indices in increasing order
            if dq and dq[0]<=i-k:
                dq.popleft()
            #drop smaller values than current value from the back
            while dq and nums[dq[-1]]<n:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                result.append(nums[dq[0]])
        return result 



    