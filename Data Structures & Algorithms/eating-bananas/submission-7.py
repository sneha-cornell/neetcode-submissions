class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles has no.of bananas in each pile 
        #h is no. of hours 
        #k is bananas/hour rate - at least least no. in any pile 
        #we want min k 

        low,high = 1,max(piles)
        #search for threshold not exact match so should be only < not <=
        while low<high:
            mid = (low+high)//2
            hours = sum(math.ceil(pile/mid) for pile in piles)
            if hours<=h:
                high=mid #mid works, try slower for min k
            else:
                low = mid +1 #mid too slow, must go faster 
        return low

