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
    # it's better to treat it as linked list,
    # see also #23 for "merge k sorted lists"

    def __init__(self):
        self.tweet_heads: Dict[int, Tweet] = {}
        self.following: Dict[int, Set[int]] = defaultdict(set)
        self.timestamp: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        new_tweet = Tweet(tweetId, self.timestamp)

        new_tweet.next = self.tweet_heads.get(userId)
        self.tweet_heads[userId] = new_tweet

        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []

        self._addUserTweetListToHeap(max_heap, userId, userId)

        for followee_id in self.following[userId]:
            self._addUserTweetListToHeap(max_heap, followee_id, followee_id)

        result = []

        for _ in range(10):
            if not max_heap:
                break

            neg_timestamp, tweet_id, tweet_node, user_id = heapq.heappop(max_heap)
            result.append(tweet_id)

            if tweet_node.next:
                next_tweet = tweet_node.next
                heapq.heappush(
                    max_heap,
                    (-next_tweet.timestamp, next_tweet.tweet_id, next_tweet, user_id),
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

    def _addUserTweetListToHeap(self, heap: List, user_id: int, original_user_id: int):
        if user_id in self.tweet_heads:
            tweet = self.tweet_heads[user_id]
            heapq.heappush(
                heap,
                (
                    -tweet.timestamp,  # negative for max heap behavior
                    tweet.tweet_id,
                    tweet,
                    user_id,
                ),
            )


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
