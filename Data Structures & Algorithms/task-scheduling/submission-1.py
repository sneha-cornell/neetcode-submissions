class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #avoid consecutive duplicates (less than n apart) to minimize idle time 
        count = Counter(tasks)
        max_freq = max(count.values())
        max_count = sum(1 for v in count.values() if v==max_freq)

        result = (max_freq-1)*(n+1)+max_count
        return max(result,len(tasks))