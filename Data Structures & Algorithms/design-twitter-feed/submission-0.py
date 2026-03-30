class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # since the user feed shall also show there own tweets, we add the user themself to the followee list
        self.followMap[userId].add(userId)

        # for each user inside the follow set
        for user in self.followMap[userId]:
            # if the user has any tweets
            if user in self.tweetMap:
                # index of this user's(followee) most recent tweet
                idx = len(self.tweetMap[user])-1
                # get the most recent tweet
                time, tweetId = self.tweetMap[user][idx]
                # push the tweet on the heap
                heapq.heappush(heap, (-time, tweetId, user, idx-1)) 
        while heap and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx >= 0:
                time, tweetId = self.tweetMap[user][idx]
                heapq.heappush(heap, (-time, tweetId, user, idx-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

