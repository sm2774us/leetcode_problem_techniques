from typing import List
import unittest

# The setup of this question is hinting for the Dictionary-based approach.
#
# Dictionary can solve any two-sum problem without using the condition of a sorted array.
#
# Rather than two-pointers or binary search based approaches both of these
# approaches involve sorting which has a worse time complexity O(Nlog(N)) and so is not optimal.
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
                    return [i, j]
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
        #         return [checker[target - num], i]
        #     checker[num] = i
        # return []
        seen = {}
        for i, value in enumerate(nums):  # 1
            remaining = target - nums[i]  # 2

            if remaining in seen:  # 3
                return [seen[remaining], i]  # 4
            else:
                seen[value] = i  # 5

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
                return [checker[num], i]
            except KeyError:
                checker[target - num] = i
        return []

    # Solution 3 : Two Pointers
    #              ( sort the array for (num, index), use two pointers to find target )
    #
    # TC: O(Nlog(N)) => O(Nlog(N)) for sort + O(N) for lookup = O(Nlog(N))
    # SC: O(N)       => for storing sorted array and  indexes of the numbers in initial array
    def twoSum_solution_3_two_pointers(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        # store val->idx in List[(int, int)]
        nums_sorted = []
        for idx, val in enumerate(nums):
            nums_sorted.append((val, idx))
        # sort
        nums_sorted.sort(key=lambda elt: elt[0])
        # two pointers
        left, right = 0, len(nums) - 1
        while left < right:
            currentSum = nums_sorted[left][0] + nums_sorted[right][0]
            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                return sorted([nums_sorted[left][1], nums_sorted[right][1]])
        return []

    # Solution 4 : Binary Search ( Conceptually similar to the hashing approach except that instead of
    #                              using a hash table, we sort the array elements and use binary search to test
    #                              if a pair appears )
    #
    # TC: O(Nlog(N)) => O(Nlog(N)) for sort + O(N) for lookup = O(Nlog(N))
    #                   for sorting and searching the sorted array
    #
    # SC: O(N)       => for storing sorted array and  indexes of the numbers in initial array
    def twoSum_solution_4_binary_search(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        new_nums = []
        for index, num in enumerate(nums):
            new_nums.append((num, index))
        new_nums.sort()
        n = len(new_nums)
        for i in range(n - 1):
            index = self.find_index(target - new_nums[i][0], new_nums, i + 1)
            if index != -1:
                return [min(new_nums[i][1], index), max(new_nums[i][1], index)]
        return []

    def find_index(self, target, nums, start):
        left, right = start, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid][0] <= target:
                left = mid
            else:
                right = mid
        if nums[left][0] == target:
            return nums[left][1]
        if nums[right][0] == target:
            return nums[right][1]
        return -1

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_twoSum(self) -> None:
        s = Solution()
        for nums, target, solution in (
            [[2, 7, 11, 15], 9, [0, 1]],        # Because nums[0] + nums[1] == 9, we return [0, 1].
            [[3, 2, 4], 6, [1, 2]],
            [[3, 3], 6, [0, 1]],
            [[1, 4, 2, 0], 3, [0, 2]],
            [[3, 5, -4, 8, 11, 1, -1, 6], 10, [4, 6]]
        ):
            self.assertEqual(solution, s.twoSum_solution_1_brute_force(nums, target))
            self.assertEqual(solution, s.twoSum_solution_2a_dictionary_lbyl_approach(nums, target))
            self.assertEqual(solution, s.twoSum_solution_2b_dictionary_eafp_approach(nums, target))
            self.assertEqual(solution, s.twoSum_solution_3_two_pointers(nums, target))
            self.assertEqual(solution, s.twoSum_solution_4_binary_search(nums, target))

if __name__ == "__main__":
    unittest.main()
