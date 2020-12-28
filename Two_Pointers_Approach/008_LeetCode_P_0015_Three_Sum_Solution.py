# LeetCode - Problem 15 - Three Sum (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
#
from typing import List
from typing import Set

import unittest

class Solution:
    # Solution             : Two-Pointers Technique
    # ----------------------
    # Solution Explanation :
    # ----------------------
    # In case some newbies like me:) are wondering:
    #
    # 1. len(nums)-2 is because we need at least 3 numbers to continue.
    # 2. if i > 0 and nums[i] == nums[i-1] is because when i = 0,
    #    it doesn't need to check if it's a duplicate element since it doesn't even have a previous
    #    element to compare with. And nums[i] == nums[i-1] is to prevent checking duplicate again.
    #    (This seems to be a good pattern which has been seen in other questions as well).
    #
    # TC: O(N^2)
    # SC: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        three_sum_set = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp < 0:
                    # because total is too big, we need to decrease one element of all 3.
                     # And because nums is sorted, only left should be increased
                    left += 1
                elif temp > 0:
                    # because total is too big, we need to decrease one element of all 3.
                    # And because nums is sorted, only right should be decreased
                    right -= 1
                else:
                    # record result.
                    three_sum_set.add((nums[i], nums[left], nums[right]))
                    # skip all duplicate element.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return [[num1, num2, num3] for num1, num2, num3 in three_sum_set]

    def two_sum(self, idx: int, nums: List[int]) -> Set[int]:
        target = -nums[idx]
        left, right = 0, len(nums) - 1
        two_sum_set = set()
        while left < right:
            if left == idx or right == idx:
                if left == idx:
                    left += 1
                else:
                    right -= 1
                continue
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                two_sum_set.add((nums[left], nums[right]))
                left += 1
                right -= 1
        return two_sum_set

    def threeSum_decomposed_as_two_sum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        nums.sort()  # help to avoid duplicate triplets
        three_sum_set = set()  # using set to hold unique triplets
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # no need to check this case becasue results would be duplicates
                continue
            two_set_sum = self.two_sum(i, nums)
            for num1, num2 in two_set_sum:
                candidates = [nums[i], num1, num2]
                candidates.sort()
                three_sum_set.add((candidates[0], candidates[1], candidates[2]))
        return [[num1, num2, num3] for num1, num2, num3 in three_sum_set]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_threeSum(self) -> None:
        sol = Solution()
        for nums, solution in (
            [[-1,0,1,2,-1,-4], [[-1, 0, 1],[-1, -1, 2]]],
            [[], []],
            [[0], []]
        ):
            self.assertEqual(solution, sol.threeSum(nums))
            self.assertEqual(solution, sol.threeSum_decomposed_as_two_sum(nums))

if __name__ == "__main__":
    unittest.main()
