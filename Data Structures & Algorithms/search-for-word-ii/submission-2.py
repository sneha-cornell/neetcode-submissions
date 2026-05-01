class TrieNode:
    def __init__(self):
        self.children={}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words: 
            node = root
            for c in w:
                if c not in node.children: 
                    node.children[c]=TrieNode()
                node = node.children[c]
            node.word = w
        rows,cols = len(board),len(board[0])
        res = set()

        def dfs(node,r,c):
            if r<0 or c<0 or r>=rows or c>=cols: 
                return 
            ch = board[r][c]
            if ch=='#' or ch not in node.children:
                return
            next_node = node.children[ch]
            if next_node.word:
                res.add(next_node.word)
            board[r][c]='#'
            dfs(next_node,r+1,c)
            dfs(next_node,r-1,c)
            dfs(next_node,r,c+1)
            dfs(next_node,r,c-1)
            board[r][c]=ch
        for r in range(rows): 
            for c in range(cols):
                dfs(root,r,c)
        return list(res)


