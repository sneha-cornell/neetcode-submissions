class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #recurse on valid combinations of parentheses pairs 
        result = []
        def backtrack(path,open_count,close_count):
            if len(path)==2*n:
                result.append("".join(path))
                return 
            if open_count<n: #can still open 
                path.append("(")
                backtrack(path,open_count+1,close_count)
                path.pop()
            if close_count<open_count: #can still close an outstanding open
                path.append(")") 
                backtrack(path,open_count,close_count+1)
                path.pop()
        backtrack([],0,0)
        return result 
                
            
