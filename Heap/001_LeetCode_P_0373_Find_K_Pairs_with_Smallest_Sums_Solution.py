# LeetCode - Problem 373 - Find K Pairs with Smallest Sums (https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
#
from typing import List
import heapq

import unittest

class Solution:
    # Solution 1 : Python heap solution
    #
    # TC: O(K*log(K))
    #
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if not nums1 or not nums2 or not k:
            return res

        heap = []
        visited = set()

        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        visited.add((0, 0))

        while len(res) < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        return res


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_kSmallestPairs(self) -> None:
        sol = Solution()
        for nums1, nums2, k, solution in (
                [[1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]],        # The first 3 pairs are returned from the sequence:
                                                                    # [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
                [[1,1,2], [1,2,3], 2, [[1,1],[1,1]]]
        ):
            self.assertEqual(solution, sol.kSmallestPairs(nums1, nums2, k))

if __name__ == "__main__":
    unittest.main()

