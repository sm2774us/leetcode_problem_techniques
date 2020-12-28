from typing import List
import unittest

# The setup of this question is highlighting the tradeoffs involved.
#
# Dictionary-based approach gives us O(N) time w/ O(N) space.
#
# Whereas, two-pointers and binary search based approaches give us O(Nlog(N)) time w/ O(1) space.
#
# So Dictionary-based approach trades time for space and also involves less code complexity.
#
# Whereas, the two-pointers and binary search based approaches trades space for time.
#
# Dictionary can solve any two-sum problem without using the condition of a sorted array.
#
class Solution:
    # Solution 1 : Brute Force
    #              (nested loop get all combination of two numbers)
    #
    # TC: O(N^2)
    # SC: O(1)
    def twoSum_solution_1_brute_force(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        for i in range(len(nums) - 1):
            firstNum = nums[i]
            for j in range(i+1, len(nums)):
                secondNum = nums[j]
                if firstNum + secondNum == target:
                    return [firstNum, secondNum]
        return []

    # Solution 2 : Dictionary
    #               ( one pass, store and find target - nums[i] same time )
    #
    # TC: O(N)
    # SC: O(N)
    def twoSum_solution_2_dictionary(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        checker = {}
        for num in nums:
            if target - num in checker:
                return [target - num, num]
            else:
                checker[num] = True
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
        #nums.sort()
        # two pointers
        left, right = 0, len(nums) - 1
        while left < right:
            currentSum = nums_sorted[left][0] + nums_sorted[right][0]
            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                res = sorted([nums_sorted[left][1], nums_sorted[right][1]])
                return [nums[res[0]], nums[res[1]]]
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
                res = [min(new_nums[i][1], index), max(new_nums[i][1], index)]
                return [nums[res[0]], nums[res[1]]]
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
            [[2, 7, 11, 15], 9, [2, 7]],        # Because nums[0] + nums[1] == 9, we return [2, 7].
            [[3, 2, 4], 6, [2, 4]],
            [[3, 3], 6, [3, 3]],
            [[1, 4, 2, 0], 3, [1, 2]],
            [[3, 5, -4, 8, 11, 1, -1, 6], 10, [11, -1]]
        ):
            self.assertEqual(solution, s.twoSum_solution_1_brute_force(nums, target))
            self.assertEqual(solution, s.twoSum_solution_2_dictionary(nums, target))
            self.assertEqual(solution, s.twoSum_solution_3_two_pointers(nums, target))
            self.assertEqual(solution, s.twoSum_solution_4_binary_search(nums, target))

if __name__ == "__main__":
    unittest.main()
