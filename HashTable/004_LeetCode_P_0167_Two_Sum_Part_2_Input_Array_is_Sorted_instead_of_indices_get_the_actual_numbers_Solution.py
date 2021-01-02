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
                return [nums[left], nums[right]]
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
                    return [nums[i], nums[mid]]
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
            [[2, 7, 11, 15], 9, [2, 7]],        # Because nums[0] + nums[1] == 9, we return [2, 7] since its not zero-based indexing.
            [[2, 3, 4], 6, [2, 4]],
            [[3, 3], 6, [3, 3]],
            [[0, 1, 2], 3, [1, 2]],
            [[-4, -1, 1, 3, 5, 6, 8, 11], 10, [-1, 11]]
        ):
            self.assertEqual(solution, s.twoSum_solution_1_brute_force(nums, target))
            self.assertEqual(solution, s.twoSum_solution_2_dictionary(nums, target))
            self.assertEqual(solution, s.twoSum_solution_3_two_pointers(nums, target))
            self.assertEqual(solution, s.twoSum_solution_4_binary_search(nums, target))

if __name__ == "__main__":
    unittest.main()
