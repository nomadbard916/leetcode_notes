#
# @lc app=leetcode id=355 lang=python3
# @lcpr version=30104
#
# [355] Design Twitter
#

# @lc code=start
import heapq
from collections import defaultdict
from typing import Dict, List, Optional, Set


class Tweet:
    def __init__(self, tweet_id: int, timestamp: int) -> None:
        self.tweet_id: int = tweet_id
        self.timestamp: int = timestamp
        self.next: Optional["Tweet"] = None


class Twitter:
    # we can choose between heap and linked list implementations
    # For interviews: Both approaches are valid, but linked list shows deeper system design thinking.
    # For production: Linked list approach is more scalable and memory-efficient.
    # For learning: Understanding both approaches gives you a more complete picture of the trade-offs involved in system design.
    # see also #23 for "merge k sorted lists"

    def __init__(self):
        self.tweet_heads: Dict[int, Tweet] = {}
        self.following: Dict[int, Set[int]] = defaultdict(set)
        self.timestamp: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        new_tweet = Tweet(tweetId, self.timestamp)

        # # Insert at head of linked list (most recent tweet becomes head)
        new_tweet.next = self.tweet_heads.get(userId)
        self.tweet_heads[userId] = new_tweet

        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Collect all relevant tweets and sort by timestamp.
        """
        # collect all tweets from user and followers
        # add user's own tweets

        all_tweets = self._collectUserTweets(userId, [])
        for followee_id in self.following[userId]:
            all_tweets = self._collectUserTweets(followee_id, all_tweets)

        # sort tweets by timestamp (most recent first)
        all_tweets.sort(key=lambda tweet: tweet.timestamp, reverse=True)

        # return up to 10 most recent tweet ids
        return [tweet.tweet_id for tweet in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

    def _collectUserTweets(self, user_id: int, tweet_list: List[Tweet]) -> List[Tweet]:
        """
        Helper method to collect all tweets from a user's linked list.
        Traverses the entire linked list and adds each tweet to the collection.
        """
        current = self.tweet_heads.get(user_id)
        while current:
            tweet_list.append(current)
            current = current.next
        return tweet_list


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
