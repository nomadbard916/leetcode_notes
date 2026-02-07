#
# @lc app=leetcode id=32 lang=python3
# @lcpr version=30305
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        * nouns and verbs
        parentheses, length, valid, substring

        * pattern keywords
        stack
        longest substring: dynamic programming, sliding window

        * constraints
        well-formed, longest, substring (must be of the parent string)

        * tricky keywords:
        substring: must be contiguous
        longest: need to track max across all possibilities

        * mental categories:
        stack based matching
        dynamic programming
        two-pass scanning (left to right, right to left)
        """

        # ! sol1: stack with index recording
        """
        Approach 2: Stack (Most Intuitive)
        Time: O(n), Space: O(n)

        Intuition: Use stack to track indices of unmatched characters.
        The distance between unmatched positions gives valid length.
        """
        # if we store char in stack and pop when matched,
        # the position is lost immediately
        # => store index instead
        # When you match a pair, pop from stack
        # The distance between current position and what's left on stack = valid length

        # init with base sentinel for length calculation
        # * ## Mental Model: The "Boundary Marker" Concept
        # Imagine you're walking and placing flags:
        # 1. **See '('?** → Place a flag at your current position
        # 2. **See ')'?** → Remove the last flag (you found its partner!)
        # 3. **Measure distance** = Current position - Nearest remaining flag
        # 4. **If no flags left?** → Place a flag here (this is a boundary wall)
        # The flags aren't the parentheses themselves—they're **position markers** showing where unmatched characters are!

        # ## Quick Reference: What Stack Contains
        # Stack NEVER stores:  '(' or ')' characters
        # Stack ALWAYS stores: Integer indices (positions)
        # Why?
        # - Characters tell you WHAT matched
        # - Indices tell you WHERE and HOW LONG the valid part is
        stack: list[int] = [-1]  # this -1 means "the actual position right before 0"
        max_len = 0
        for i, char in enumerate(s):
            # Why we push indices of '(' but not ')'
            # Listen to this pattern:
            # '(' = "Start a timer" → Remember when it started (push index)
            # ')' = "Stop the timer" → Calculate duration (pop and measure)
            # You only need to remember when things started, not when they ended!
            if char == "(":
                stack.append(i)
                continue

            # char == ')', matched and pop the opening
            stack.pop()

            # special case: when a ')' is at the beginning and the sentinel is popped,
            # it becomes the new base sentinel for the beginning;
            # all the calculations for local max are reset.
            if not stack:
                stack.append(i)
                continue

            # length calculation:
            # 🎧 Audio-Oriented Explanation
            # Think of it like measuring a song's duration:
            # ❌ Character approach = Counting how many notes you played
            # - You: "I played 10 notes!"
            # - But: Were they continuous? Or did you pause?
            # - You don't know the actual song length!
            # ✅ Index approach = Looking at the timestamps
            # - Song starts at 0:05, ends at 0:23
            # - Duration = 0:23 - 0:05 = 18 seconds
            # - You know exactly how long the continuous segment is!

            # The Three Key Insights
            # 1️⃣ Why we need a "base" (-1 initially)
            # Think of -1 as "before the song started"
            # Without -1, when everything matches perfectly,
            # your stack becomes empty and you can't calculate distance!
            # 2️⃣ Why we push indices of '(' but not ')'
            # Listen to this pattern:
            # - '(' = "Start a timer" → Remember when it started (push index)
            # - ')' = "Stop the timer" → Calculate duration (pop and measure)
            # You only need to remember when things started, not when they ended!
            # 3️⃣ The "new base" trick
            # When you see ')' with no matching '(':
            # It's like saying: "This unmatched character is a wall. Anything valid must come AFTER this point."

            # Current index - index of last unmatched character
            # there should've been a "+1" for distance calculation,
            # but it's done automatically by the sentinel
            max_len = max(max_len, i - stack[-1])

        return max_len

        # ! sol2: Alternative Stack method Without Sentinel (More Code, Less Elegant)
        # You can avoid the sentinel, but look at the mess:
        stack = []
        max_length = 0
        last_unmatched = -1  # Separate variable!

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        length = i - stack[-1]  # Case 1
                    else:
                        length = i - last_unmatched  # Case 2 - different logic!
                    max_length = max(max_length, length)
                else:
                    last_unmatched = i  # Case 3 - more tracking!

        return max_length

        # ! sol3: dynamic programming
        if not s:
            return 0

        n = len(s)
        # dp[i] = longest valid ending at i
        dp: list[int] = [0] * n
        max_len = 0

        for i in range(1, n):
            # only ')' can end a valid substring
            if s[i] == "(":
                continue

            if s[i - 1] == "(":
                # case 1: ...()
                # current pair adds 2, plus whatever was before this pair
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2

            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                # Case 2: ...))
                # Example: "()(())"
                #              ^
                # We need to check if there's a matching '(' before the
                # valid substring that ends at i-1

                # Length = the valid substring ending at i-1
                #        + 2 (current matching pair)
                #        + whatever valid substring before the matching '('
                dp[i] = dp[i - 1] + 2
                if i - dp[i - 1] - 2 >= 0:
                    dp[i] += dp[i - dp[i - 1] - 2]

            max_len = max(max_len, dp[i])

        return max_len

        #  Why you got stuck
        # Your code uses a boolean (is_open) and a stack of characters, then measures len(stack) for the answer. That fails because:

        # A single boolean can't remember multiple unmatched '(', so nested or non-alternating patterns break your logic.
        # Storing characters and using len(stack) doesn't give the substring length (you need indices to compute lengths reliably).
        # it breaks at "(()"  and "()(())"
        # if len(s) == 0:
        #     return 0

        # longest = 0

        # OPEN = "("
        # CLOSED = ")"

        # # when finalized, clean up the stack and update longest.

        # stack: list[str] = []
        # is_open = False
        # for p in s:
        #     if p == OPEN:
        #         is_open = True
        #         stack.append(p)
        #         continue

        #     if is_open and p == CLOSED:
        #         is_open = False
        #         stack.append(p)

        #     longest = max(longest, len(stack))

        # return longest


# @lc code=end


#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

#
