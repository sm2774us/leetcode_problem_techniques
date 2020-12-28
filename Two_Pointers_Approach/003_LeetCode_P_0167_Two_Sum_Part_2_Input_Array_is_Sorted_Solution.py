from typing import List
import unittest

# The setup of this question is hinting for the two-pointers approach as opposed
# to the dictionary or binary search approach.
#
# Dictionary can solve any two-sum problem without using the condition of a sorted array,
# and the binary search has worse time complexity O(Nlog(N)) is not optimal.
#
class Solution:
    # Solution 1 : Brute Force
    #              (nested loop get all combination of two numbers)
    #
    # TC: O(N^2)    : because there is only n * (n - 1) / 2 combinations
    # SC: O(1)      : we occupy no extra space in memory
    def twoSum_solution_1_brute_force(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        for i in range(len(nums) - 1):
            firstNum = nums[i]
            for j in range(i+1, len(nums)):
                secondNum = nums[j]
                if firstNum + secondNum == target:
                    return [i+1, j+1]
        return []

    # Solution 2a : Dictionary ( Hashing ) using LBYL
    #               ( one pass, store and find target - nums[i] same time )
    # TC: O(N)
    # SC: O(N)
    def twoSum_solution_2a_dictionary_lbyl_approach(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        # checker = {}
        # for i, num in enumerate(nums):
        #     if target - num in checker:
        #         return [checker[target - num]+1, i+1]
        #     checker[num] = i
        # return []
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [seen[remaining] + 1, i + 1]  # 4
            else:
                seen[value] = i

    # Solution 2b : Dictionary ( Hashing ) using EAFP (PEP8)
    #               ( one pass, store and find target - nums[i] same time )
    #
    # TC: O(N)
    # SC: O(N)
    def twoSum_solution_2b_dictionary_eafp_approach(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        checker = {}
        for i, num in enumerate(nums):
            try:
                return [checker[num]+1, i+1]
            except KeyError:
                checker[target - num] = i
        return []

    # Solution 3 : Two Pointers
    #
    # TC: O(N)
    # SC: O(1)
    def twoSum_solution_3_two_pointers(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        left, right = 0, len(nums) - 1
        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == target:
                return [left + 1, right + 1]
            elif currentSum < target:
                left += 1
            else:
                right -= 1
        return []

    # Solution 4 : Binary Search ( Conceptually similar to the hashing approach except that instead of
    #                              using a hash table, we sort the array elements and use binary search to test
    #                              if a pair appears )
    #
    # TC: O(Nlog(N))
    # SC: O(1)
    def twoSum_solution_4_binary_search(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            tmp = target - nums[i]
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == tmp:
                    return [i + 1, mid + 1]
                elif nums[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1
        return []

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_twoSum(self) -> None:
        s = Solution()
        for nums, target, solution in (
            [[2, 7, 11, 15], 9, [1, 2]],        # Because nums[0] + nums[1] == 9, we return [1, 2] since its not zero-based indexing.
            [[2, 3, 4], 6, [1, 3]],
            [[3, 3], 6, [1, 2]],
            [[0, 1, 2], 3, [2, 3]],
            [[-4, -1, 1, 3, 5, 6, 8, 11], 10, [2, 8]]
        ):
            self.assertEqual(solution, s.twoSum_solution_1_brute_force(nums, target))
            self.assertEqual(solution, s.twoSum_solution_2a_dictionary_lbyl_approach(nums, target))
            self.assertEqual(solution, s.twoSum_solution_2b_dictionary_eafp_approach(nums, target))
            self.assertEqual(solution, s.twoSum_solution_3_two_pointers(nums, target))
            self.assertEqual(solution, s.twoSum_solution_4_binary_search(nums, target))

if __name__ == "__main__":
    unittest.main()
