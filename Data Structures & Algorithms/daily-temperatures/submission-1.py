class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use stack to have the unresolved days
        #before pushing today's temp, pop any colder days first 
        #stack has decreasing temps from bottom to top 

        result = [0]*len(temperatures)
        stack=[]

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                idx = stack.pop()
                result[idx]=i-idx
            stack.append(i)
        return result