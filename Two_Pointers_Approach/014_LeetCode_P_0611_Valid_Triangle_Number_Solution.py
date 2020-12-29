# LeetCode - Problem 611 - Valid Triangle Number (https://leetcode.com/problems/valid-triangle-number/)
from typing import List

import unittest

class Solution:
    # Solution 1 : 3Sum based approach ( uses Two Pointers Technique )
    #
    def triangleNumber(self, nums: List[int]) -> int:
        def two_sum_greater_than(nums, target_idx):
            target, low, high = nums[target_idx], target_idx + 1, len(nums) - 1
            count = 0
            while low < high:
                if nums[low] + nums[high] > target:
                    count += (high - low)
                    low += 1
                else:
                    high -= 1
            return count

        nums.sort(reverse=True)
        return sum(two_sum_greater_than(nums, i) for i in range(len(nums) - 2))

    # Solution 2 : Backtracking based approach - Less efficient
    #
    def triangleNumber_using_backtracking(self, nums: List[int]) -> int:
        def is_valid_triange(a, b, c):
            return (a < b + c) and (b < a + c) and (c < a + b)

        def helper(nums, i, partial_set):
            if len(partial_set) == 3:
                if is_valid_triange(*partial_set[:]):
                    self.valid_count += 1
                return

            for j in range(i, len(nums)):
                helper(nums, j + 1, partial_set + [nums[j]])

        self.valid_count = 0
        helper(nums, 0, [])
        return self.valid_count


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_triangleNumber(self) -> None:
        sol = Solution()
        nums = [2,2,3,4]
        self.assertEqual(3, sol.triangleNumber(nums))
        self.assertEqual(3, sol.triangleNumber_using_backtracking(nums))


if __name__ == "__main__":
    unittest.main()

