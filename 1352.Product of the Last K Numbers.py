#
# @lc app=leetcode id=1352 lang=python3
# @lcpr version=30104
#
# [1352] Product of the Last K Numbers
#

# @lc code=start
class ProductOfNumbers:
    def __init__(self):
        self.prefix_prod_arr = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prod_arr = [1]
        else:
            self.prefix_prod_arr.append(self.prefix_prod_arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_prod_arr):
            return 0

        return self.prefix_prod_arr[-1] // self.prefix_prod_arr[-1 - k]

    # Time Complexity:
    # add: O(1) - constant time to append to the list or reset it
    # getProduct: O(1) - constant time lookup and division

    # Space Complexity:
    # O(n) - where n is the number of consecutive non-zero numbers added


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end
