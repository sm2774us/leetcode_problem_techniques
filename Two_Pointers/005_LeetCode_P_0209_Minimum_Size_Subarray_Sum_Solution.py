# LeetCode - Problem 209 - Minimum Size Subarray Sum (https://leetcode.com/problems/minimum-size-subarray-sum/)
#
from typing import List
from math import inf

import unittest

class Solution:
    # Solution : Two-Pointers Technique
    #
    # TC: O(N)
    # SC: O(N)
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = inf
        left = 0
        curr_s = 0
        for right in range(len(nums)):
            curr_s += nums[right]
            while curr_s >= s:
                res = min(res, right - left + 1)
                curr_s -= nums[left]
                left += 1
        return res if res != inf else 0


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxSubArrayLen(self) -> None:
        sol = Solution()
        for s, nums, solution in (
            [7, [2,3,1,2,4,3], 2],          # Because the the subarray [4,3] has the minimal length under the problem constraint.
            [11, [2,3,4,1,3,6], 4]
        ):
            self.assertEqual(solution, sol.minSubArrayLen(s, nums))

if __name__ == "__main__":
    unittest.main()
