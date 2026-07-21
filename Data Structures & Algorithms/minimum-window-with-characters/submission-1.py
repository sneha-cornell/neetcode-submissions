class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #reuse window state incrementally and monotonic pointers (only shrink when valid - 2n not n^2)
        if not s or not t: 
            return ""
        need = Counter(t)
        missing = len(t)
        left = 0
        best_len = float('inf')
        best_start=0

        for right,ch in enumerate(s):
            if need[ch]>0:
                missing-=1
            need[ch]-=1 #can go negative

            #window is valid
            while missing==0:
                if right-left+1<best_len:
                    best_len = right-left+1
                    best_start=left #try to shrink from left 
                need[s[left]]+=1
                if need[s[left]]>0:
                    missing+=1
                left+=1
        return "" if best_len==float('inf') else s[best_start:best_start+best_len] 

