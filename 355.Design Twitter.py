#
# @lc app=leetcode id=355 lang=python3
# @lcpr version=30104
#
# [355] Design Twitter
#

# @lc code=start
from collections import defaultdict
from typing import Dict, List, Optional, Set


class Tweet:
    def __init__(self, tweet_id: int, timestamp: int) -> None:
        self.tweet_id: int = tweet_id
        self.timestamp: int = timestamp
        self.next: Optional["Tweet"] = None  # Points to next older tweet


class Twitter:
    # we can choose between heap and linked list implementations
    # For interviews: Both approaches are valid, but linked list shows deeper system design thinking.
    # For production: Linked list approach is more scalable and memory-efficient.
    # For learning: Understanding both approaches gives you a more complete picture of the trade-offs involved in system design.
    # see also #23 for "merge k sorted lists"

    def __init__(self):
        # Store head of tweet linked list for each user: user_id -> Tweet node
        self.tweet_heads: Dict[int, Tweet] = {}
        # Store who each user follows: user_id -> set of followed user_ids
        self.following: Dict[int, Set[int]] = defaultdict(set)
        # Global timestamp counter to maintain chronological order
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
        # add user's own tweets, starting from an empty list container
        all_tweets = self._collectUserTweets(userId, [])
        for followee_id in self.following[userId]:
            # add tweets for each followee
            all_tweets = self._collectUserTweets(followee_id, all_tweets)

        # sort tweets by timestamp (most recent first)
        all_tweets.sort(key=lambda tweet: tweet.timestamp, reverse=True)

        # return up to 10 most recent tweet ids
        return [tweet.tweet_id for tweet in all_tweets[:10]]

        """
        Alternative optimized version that stops early when we have enough tweets.
        Uses a more sophisticated approach to avoid collecting all tweets.
        """
        result = []

        # Create list of current tweet pointers for each user
        tweet_pointers = []

        # Add user's own tweet list
        if userId in self.tweet_heads:
            tweet_pointers.append(self.tweet_heads[userId])

        # Add tweet lists from all followed users
        for followee_id in self.following[userId]:
            if followee_id in self.tweet_heads:
                tweet_pointers.append(self.tweet_heads[followee_id])

        # Get 10 most recent tweets by repeatedly finding the most recent among current pointers
        for _ in range(10):
            if not tweet_pointers:
                break

            # Find the tweet with the highest timestamp among current pointers
            max_timestamp = -1
            max_tweet = None
            max_index = -1

            for i, tweet in enumerate(tweet_pointers):
                if tweet and tweet.timestamp > max_timestamp:
                    max_timestamp = tweet.timestamp
                    max_tweet = tweet
                    max_index = i

            if max_tweet is None:
                break

            # Add this tweet to result
            result.append(max_tweet.tweet_id)

            # Move the pointer to next tweet in that user's list
            if max_tweet.next:
                tweet_pointers[max_index] = max_tweet.next
            else:
                # Remove this pointer if no more tweets
                tweet_pointers.pop(max_index)

        return result

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
