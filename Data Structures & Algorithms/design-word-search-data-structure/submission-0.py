class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False
        

    def addWord(self, word: str) -> None:
        node = self
        for c in word: 
            if c not in node.children: 
                node.children[c]=WordDictionary()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for i,c in enumerate(word):
            if c=='.':
                for child in node.children.values():
                    if child.search(word[i+1:]):
                        return True
                return False
            if c not in node.children: 
                return False
            node = node.children[c]
        return node.is_end

        
