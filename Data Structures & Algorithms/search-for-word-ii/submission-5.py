# change the node structure because it saves the cost of string concatenation 
# when we have to eventually append the node to the result
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # store the whole word here for dfs optimization

class Solution:

    def build_trie(self, words: List[str]) -> TrieNode:
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()         
                node = node.children[ch]
            node.word = word
        
        return root
            
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # unrequired empty check
        if not board or not board[0] or not words:
            return []

        rows, cols = len(board), len(board[0])
        root = self.build_trie(words)
        res = []
        

        def dfs(node: TrieNode, r: int, c: int) -> None:
            # out of bounds check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # current char
            ch = board[r][c]

            # skip/prune
            if ch == "#" or ch not in node.children:
                return

            # traversal
            nxt = node.children[ch]

            # prevent deduplication and optimze dfs append to result instead of building string just append the word
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None

            # mark as visited
            board[r][c] = '#'

            # traverse different branches
            dfs(nxt, r + 1, c)
            dfs(nxt, r - 1, c)
            dfs(nxt, r, c + 1)
            dfs(nxt, r, c - 1)

            # restore the marked value
            board[r][c] = ch
            
            # prunce unwanted node
            if not nxt.children and nxt.word is None:
                del node.children[ch]

        for r in range(rows):
           for c in range(cols):
               dfs(root, r, c)
    
        return res
                
            