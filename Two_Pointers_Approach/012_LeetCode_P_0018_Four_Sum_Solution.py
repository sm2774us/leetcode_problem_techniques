# LeetCode - Problem 16 - Three Sum Closest (https://leetcode.com/problems/3sum-closest/)
#
from typing import List
from math import inf

import unittest

class Solution:
    # Solution : Two-Pointers Technique
    #
    # TC: O(N^2)
    # SC: O(1)
    #
    # Follow-up Question: Can we do better than O(N^2) ?
    # -------------------
    # Answer            : No there isn't. Proof by contradiction:
    # -------------------
    #                     If we had sub-quadratic solution to this problem then we could solve all instances
    #                     of 3SUM problem with the same complexity (sub-quadratic),
    #                     but lower bound of 3SUM problem is O(N^2).
    #
    # NOTE:
    # -------------------
    # You can get some improvement by skipping the duplicate value while i++,
    # it certainly saves time as you don't need to enter the sub-iteration each time.
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: return
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):

            # update: ignore the duplicate numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                curSum = nums[left] + nums[right] + nums[i]
                if curSum == target:
                    return target
                if abs(curSum - target) < abs(result - target):
                    result = curSum
                if curSum < target:
                    left += 1
                else:
                    right -= 1
        return result


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_threeSumClosest(self) -> None:
        sol = Solution()
        for nums, target, solution in (
            [[-1,2,1,-4], 1, 2],            # The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
            [[-1,8,3,-2], 4, 5]
        ):
            self.assertEqual(solution, sol.threeSumClosest(nums, target))

if __name__ == "__main__":
    unittest.main()
