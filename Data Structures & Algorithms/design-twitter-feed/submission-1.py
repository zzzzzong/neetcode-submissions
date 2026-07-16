class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)
        self.timestamp = 0 
        

    def postTweet(self, userId: int, tweetId: int) -> None: 
        self.posts[userId].append([self.timestamp, tweetId])   
        self.timestamp += 1 
        # print("post added for", userId, self.posts)      


    def getNewsFeed(self, userId: int) -> List[int]: 
        # Max heap (use negative timestamp for min-heap to act as max-heap)
        feed = []
        
        # Get tweets from user's own posts
        for ts, tweetId in self.posts[userId]:
            heapq.heappush(feed, (-ts, tweetId))
        
        # Get tweets from followees
        for followee in self.follows[userId]:
            for ts, tweetId in self.posts[followee]:
                heapq.heappush(feed, (-ts, tweetId))
        
        # Extract top 10 most recent tweets
        result = []
        while feed and len(result) < 10:
            _, tweetId = heapq.heappop(feed)
            result.append(tweetId)
        
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None: 
        if followerId != followeeId: 
            self.follows[followerId].add(followeeId)   
            # print("follow:", followerId, followeeId, self.follows)      


    def unfollow(self, followerId: int, followeeId: int) -> None: 
        if followerId != followeeId: 
            self.follows[followerId].discard(followeeId)   
            # print("unfollow:", followerId, followeeId, self.follows)      
        
