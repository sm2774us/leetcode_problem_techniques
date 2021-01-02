# LeetCode - Problem 325 - Maximum Size Subarray Sum Equals k
#
# Description: Given an array nums and target value k, find the maximum length of a sub-array that sums to k.
#              If there isn’t one, return 0 instead.
#
# Note: The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
#
# Example:
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4
#
# Analysis:
# Whenever we see a problem of finding sub-array of sum k.
# We need to immediately think of the following two ways to solve it.
#
# 1) Method 1: Brute-Force ( Every sub-array )       => TC: O(N^2) ; SC: O(1)
# 2) Method 2: HashTable                            => TC: O(N)   ; SC: O(N)
#
# NOTE: For any sub-array problems, we need to instantly realize that indexes/positions/order
#       of the elements are important.
#       Hence, we cannot sort, which would disrupt the order of the elements
#
from typing import List
import unittest

# Dictionary can solve any two-sum problem without using the condition of a sorted array.
#

# Example 1: Given nums = [1, -1, 5, -2, 3], k = 3, return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
#
# Example 2: Given nums = [-2, -1, 2, 1], k = 1, return 2. (because the subarray [-1, 2] sums to 1 and is the longest)
#
class Solution:
    # Solution 1 : Brute Force
    #              (nested loop get all combination of two numbers)
    #
    # TC: O(N^2)    : because there is only n * (n - 1) / 2 combinations
    # SC: O(1)      : we occupy no extra space in memory
    def maxSubArrayLen_solution_1_brute_force(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        ans = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    ans = max(ans, j - i + 1)
        return ans

    # Solution 2 : Dictionary
    #
    # TC: O(N)
    # SC: O(N)
    def maxSubArrayLen_solution_2_dictionary(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {}
        cur_sum, max_len = 0, 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum == k:
                max_len = i + 1
            elif cur_sum - k in sums:
                max_len = max(max_len, i - sums[cur_sum - k])
            if cur_sum not in sums:
                sums[cur_sum] = i  # Only keep the smallest index.
        return max_len


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxSubArrayLen(self) -> None:
        s = Solution()
        for nums, k, solution in (
            [[1, -1, 5, -2, 3], 3, 4],        # Because the subarray [1, -1, 5, -2] sums to 3 and is the longest.
            [[-2, -1, 2, 1], 1, 2]            # Because the subarray [-1, 2] sums to 1 and is the longest.
        ):
            self.assertEqual(solution, s.maxSubArrayLen_solution_1_brute_force(nums, k))
            self.assertEqual(solution, s.maxSubArrayLen_solution_2_dictionary(nums, k))

if __name__ == "__main__":
    unittest.main()
