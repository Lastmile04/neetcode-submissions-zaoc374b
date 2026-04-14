# <--Frist thoughts about the problem-->
'''
the main hurdal in this problem is to build an adjacency list/graph
after that is built then it's simply using bfs/dfs traversal to find the shortest path
'''
# Approach
'''
BFS:
# initiate the dictionary
# append the beginWord for easire traversal
# loop each word then to each char for creating pattern
# use the patter to append neighbour in dictionary
#  
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        if beginWord not in wordList:
            wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                # left + "*" + right
                pattern = word[:i] + '*' + word[i+1:]
                nei[pattern].append(word)
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
                    nei[pattern] = []
            res+=1
        return 0

