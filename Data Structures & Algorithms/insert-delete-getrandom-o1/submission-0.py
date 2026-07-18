#array instead of DLL as it is O(1) random access but DLL is O(n)

import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map ={}

    def insert(self, val: int) -> bool:
        if val in self.map: 
            return False
        self.map[val]=len(self.arr)
        self.arr.append(val)
        return True 


    def remove(self, val: int) -> bool:
        if val not in self.map: 
            return False
        #to ensure we pop from end to have O(1) instead of O(n)
        idx = self.map[val]
        last = self.arr[-1]
        #list index assignment 
        self.arr[idx]=last
        #map index assignment 
        self.map[last]=idx
        self.arr.pop()
        del self.map[val]
        return True 
        
    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()