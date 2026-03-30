class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        
        def dfs(node, idx):
            # base case
            if idx == len(word):
                return node.end

            # CASE 1: if the current ch is '.'
            if word[idx] == '.':
                for ch in node.children.values():
                    if dfs(ch, idx+1):
                        return True
                return False
            # CASE 2: if the ch is normal char
            else:
                if word[idx] not in node.children:
                    return False
                return dfs(node.children[word[idx]], idx+1)

        return dfs(self.root, 0)






            

