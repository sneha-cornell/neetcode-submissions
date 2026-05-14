class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.followers =defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.timestamp,tweetId))
        self.timestamp+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap =[]
        users=self.followers[userId] | {userId}

        for uid in users: 
            if self.tweets[uid]:
                idx = len(self.tweets[uid])-1
                time,tweetId = self.tweets[uid][idx]
                heapq.heappush(heap,(time,tweetId,uid,idx))
        result =[]
        while heap and len(result)<10:
            time,tweetId,uid,idx = heapq.heappop(heap)
            result.append(tweetId)
            if idx>0: 
                idx-=1
                time,tweetId = self.tweets[uid][idx]
                heapq.heappush(heap,(time,tweetId,uid,idx))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
