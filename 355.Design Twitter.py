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
        Uses merge k sorted lists approach where each user's tweets form a sorted linked list.
        """
        # Max heap to merge multiple sorted linked lists
        # Format: (-timestamp, tweet_id, tweet_node, user_id)
        max_heap = []

        # Add user's own tweet list head to heap
        self._addUserTweetListToHeap(max_heap, userId, userId)

        # Add tweet list heads from all followed users
        for followee_id in self.following[userId]:
            self._addUserTweetListToHeap(max_heap, followee_id, followee_id)

        # Extract up to 10 most recent tweets using merge approach
        result = []
        for _ in range(10):
            if not max_heap:
                break

            # Get most recent tweet
            neg_timestamp, tweet_id, tweet_node, user_id = heapq.heappop(max_heap)
            result.append(tweet_id)

            # Add next older tweet from same user if exists
            if tweet_node.next:
                next_tweet = tweet_node.next
                heapq.heappush(
                    max_heap,
                    (-next_tweet.timestamp, next_tweet.tweet_id, next_tweet, user_id),
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

    def _addUserTweetListToHeap(self, heap: List, user_id: int, original_user_id: int):
        """
        Helper method to add the head of a user's tweet linked list to the heap.

        Args:
            heap: The heap to add to
            user_id: The user whose tweets we're adding
            original_user_id: For tracking purposes (could be follower or followee)
        """
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
