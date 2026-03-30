# change the node structure because it saves the cost of string concatenation 
# when we have to eventually append the node to the result
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # store the whole word here for dfs optimization

class Solution:
    
    def __init__(self):
        self.root = TrieNode()

    def buildTrie(self, words):

        for word in words:
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()         
                node = node.children[ch]
            node.word = word
            
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        self.buildTrie(words)
        rowLen = len(board)
        colLen = len(board[0])
        

        def dfs(node, r, c):

            # out of bounds check
            if (r >= rowLen or
                r < 0 or 
                c >= colLen or
                c < 0
            ):
                return

            # current char
            ch = board[r][c]

            # skip/prune
            if ch not in node.children:
                return

            # traversal
            node = node.children[ch]

            # prevent deduplication and optimze dfs append to result instead of building string just append the word
            if node.word:
                res.append(node.word)
                node.word = None

            # mark as visited
            board[r][c] = '#'

            # traverse different branches
            dfs(node, r+1, c)
            dfs(node, r-1, c)
            dfs(node, r, c+1)
            dfs(node, r, c-1)

            # restore the marked value
            board[r][c]= ch

        for r in range(rowLen):
            for c in range(colLen):
                dfs(self.root, r, c)
        return res
                
            