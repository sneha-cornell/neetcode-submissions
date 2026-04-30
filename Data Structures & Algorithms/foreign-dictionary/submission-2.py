class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    graph[w1[j]].add(w2[j]) 
                    break
        state = {}
        res = []
        def dfs(c):
            if c in state: 
                return state[c]!=1
            state[c]=1
            for neighbor in graph[c]:
                if not dfs(neighbor):
                    return False
            state[c]=2
            res.append(c)
            return True
        for c in graph: 
            if not dfs(c):
                return ""
        return "".join(reversed(res))
