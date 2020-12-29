# LeetCode - Problem 494 - Target Sum (https://leetcode.com/problems/target-sum/)
from typing import List

import unittest

class Solution:
    # Solution 1: DP top-down
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        index = len(nums) - 1
        curr_sum = 0
        return self.dp(nums, S, index, curr_sum)

    def dp(self, nums: List[int], target: int, index: int, curr_sum: int) -> int:
        # Base Cases
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0

        # Decisions
        positive = self.dp(nums, target, index - 1, curr_sum + nums[index])
        negative = self.dp(nums, target, index - 1, curr_sum + -nums[index])

        return positive + negative

    # Solution 2: DP top-down w/ memoization
    def findTargetSumWays_with_memoization(self, nums: List[int], S: int) -> int:
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp_with_memoization(nums, S, index, curr_sum)

    def dp_with_memoization(self, nums: List[int], target: int, index: int, curr_sum: int) -> int:
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0

        positive = self.dp_with_memoization(nums, target, index - 1, curr_sum + nums[index])
        negative = self.dp_with_memoization(nums, target, index - 1, curr_sum + -nums[index])

        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findTargetSumWays(self) -> None:
        sol = Solution()
        nums = [1, 1, 1, 1, 1]
        S = 3
        self.assertEqual(5, sol.findTargetSumWays(nums, S))
        self.assertEqual(5, sol.findTargetSumWays_with_memoization(nums, S))


if __name__ == "__main__":
    unittest.main()

