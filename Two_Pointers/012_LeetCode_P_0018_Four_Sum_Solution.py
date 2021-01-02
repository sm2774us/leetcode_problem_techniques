# LeetCode - Problem 18 - 4Sum (https://leetcode.com/problems/4sum/)
#
from typing import List

import unittest

class Solution:
    # Solution 1 : Iterative Solution
    #
    # TC: O(N^3)
    #
    def fourSum_iterative_solution(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        L = len(nums)
        res = []
        while i < L - 3:
            if target - nums[i] < 3 * nums[i + 1] or target - nums[i] > 3 * nums[-1]:   # key judgement
                while i < L - 4 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
                continue
            j = i + 1
            while j < L - 2:
                if target - nums[i] - nums[j] < 2 * nums[j + 1] or target - nums[i] - nums[j] > 2 * nums[-1]: # key judgement
                    while j < L - 3 and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    continue
                left = j + 1
                right = L - 1
                new_target = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] > new_target:
                        right -= 1
                    elif nums[left] + nums[right] < new_target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        temp_left = nums[left]
                        temp_right = nums[right]
                        while (left < right and nums[left] == temp_left):
                            left += 1
                        while (left < right and nums[right] == temp_right):
                            right -= 1
                while j < L - 3 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i < L - 4 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

    # Solution 2 : Decomposition into 2Sum problem ( Recursive )
    #
    # TC: O(N^3)
    #
    def fourSum_recursive_solution(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(nums, target, N, cur):
            if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:  # if minimum possible sum (every element is first element) > target
                return  # or maximum possible sum (every element is first element) < target, it's impossible to get target anyway
            if N == 2:  # 2-sum problem
                left, right = 0, len(nums) - 1
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        res.append(cur + [nums[left], nums[right]])
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
            else:  # reduce to N-1 sum problem
                for i in range(len(nums) - N + 1):
                    if i == 0 or nums[i - 1] != nums[i]:
                        findNsum(nums[i + 1:], target - nums[i], N - 1, cur + [nums[i]])

        res = []
        findNsum(sorted(nums), target, 4, [])
        return res


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_fourSum(self) -> None:
        sol = Solution()
        for nums, target, solution in (
            [[1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]],
            [[], 0, []]
        ):
            self.assertEqual(solution, sol.fourSum_iterative_solution(nums, target))
            self.assertEqual(solution, sol.fourSum_recursive_solution(nums, target))

if __name__ == "__main__":
    unittest.main()
