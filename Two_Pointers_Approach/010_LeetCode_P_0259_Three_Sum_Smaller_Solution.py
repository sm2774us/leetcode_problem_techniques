# LeetCode - Problem 259 - 3Sum Smaller (https://leetcode.com/problems/3sum-smaller/)
#
from typing import List

import unittest

class Solution:
    # Solution : Two-Pointers Technique
    #
    # TC: O(N^2)
    # SC: O(1)
    #
    # NOTE:
    # -------------------
    # You can get some improvement by skipping the duplicate value while i++,
    # it certainly saves time as you don't need to enter the sub-iteration each time.
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3: return 0

        nums.sort()
        result = 0
        for i, num in enumerate(nums):
            # update: ignore the duplicate numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Now we need to find a combination of two numbers
            # that combined equal to less than (target-num) in the subscript greater than i
            t = target - num

            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] >= t:
                    right -= 1  # The sum is too big, try to reduce the sum
                elif nums[left] + nums[right] < t:
                    result += right - left  # In this case, left can form a set of answers with any number between [left + 1, right]
                    left += 1

        return result

    def twoSumSmaller(self, nums: List[int], target: int) -> int:
        sums = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                sums += right - left
                left += 1
            else:
                right -= 1

        return sums

    # Solution : Decomposition into 2Sum Problem
    #
    # TC: O(N^2)
    # SC: O(1)
    #
    # NOTE:
    # -------------------
    # You can get some improvement by skipping the duplicate value while i++,
    # it certainly saves time as you don't need to enter the sub-iteration each time.
    def threeSumSmaller_decomposed_as_two_sum(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3: return 0

        sums = 0
        nums.sort()
        for i in range(len(nums) - 2):
            # update: ignore the duplicate numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            sums += self.twoSumSmaller(nums[i + 1:], target - nums[i])

        return sums

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_threeSumSmaller(self) -> None:
        sol = Solution()
        for nums, target, solution in (
            [[-2,0,1,3], 2, 2],            # Because there are two triplets which sums are less than 2:
                                           # [-2,0,1] and [-2,0,3]
            [[-1,8,3,-2], 9, 2],
            [[-1,-1,-1], -2, 1],
            [[1,1,1], 4, 1]
        ):
            self.assertEqual(solution, sol.threeSumSmaller(nums, target))
            self.assertEqual(solution, sol.threeSumSmaller_decomposed_as_two_sum(nums, target))

if __name__ == "__main__":
    unittest.main()
