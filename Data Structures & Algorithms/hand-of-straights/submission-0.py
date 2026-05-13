from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize!=0:
            return False
        count = Counter(hand)
        sorted_keys = sorted(count)

        for card in sorted_keys: 
            if count[card]>0:
                freq = count[card]
                for i in range(groupSize):
                    if count[card+i]<freq: 
                        return False
                    count[card+i]-=freq
        return True
