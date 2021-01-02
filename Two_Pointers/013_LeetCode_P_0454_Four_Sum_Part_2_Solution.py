# LeetCode - Problem 454 - 4Sum II (https://leetcode.com/problems/4sum-ii/)
#
from typing import List
import collections

import unittest

class Solution:
    # Solution 1 : Hash table solution
    #
    # TC: O(N^2)
    #
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashmap = collections.defaultdict(int)
        for a in A:
            for b in B:
                hashmap[a + b] += 1
        count = 0
        for c in C:
            for d in D:
                count += hashmap[-c - d]
        return count

    def fourSumCount_two_liner(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sums = collections.Counter(c + d for c in C for d in D)
        return sum(sums.get(-(a + b), 0) for a in A for b in B)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_fourSumCount(self) -> None:
        #
        # Input:
        # A = [ 1, 2]
        # B = [-2,-1]
        # C = [-1, 2]
        # D = [ 0, 2]
        #
        # Output:
        # 2
        #
        # Explanation:
        # The two tuples are:
        # 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
        # 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
        #
        sol = Solution()
        A = [1, 2]
        B = [-2, -1]
        C = [-1, 2]
        D = [0, 2]
        self.assertEqual(2, sol.fourSumCount(A, B, C, D))
        self.assertEqual(2, sol.fourSumCount_two_liner(A, B, C, D))


if __name__ == "__main__":
    unittest.main()
