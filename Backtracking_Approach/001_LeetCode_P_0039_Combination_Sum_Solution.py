# LeetCode - Problem 40 - Combination Sum II (https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
#
from typing import List
import collections

import unittest

class Solution:
    # Solution 1 : Backtracking solution
    #
    # TC: O(K*log(K))
    #
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(left, path, idx):
            if not left:
                res.append(path[:])
            else:
                for i, val in enumerate(candidates[idx:]):
                    if val > left: break
                    dfs(left - val, path + [val], idx + i)

        dfs(target, [], 0)
        return res

    # Solution 1 : DP solution
    #
    # TC: O(K*log(K))
    #
    def combinationSum_using_DP(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort()
        # dp = [[[]]] + [[] for i in range(target)]
        # for i in range(1, target + 1):
        #     for number in candidates:
        #         if number > i: break
        #         for L in dp[i - number]:
        #             if not L or number >= L[-1]: dp[i] += L + [number],
        # return dp[target]
        counter = collections.Counter(candidates)
        dp = [[[]]] + [[] for _ in range(target + 1)]
        for c, cnt in counter.items():
            for i in range(c, target + 1):
                dp[i].extend([arr + [c] for arr in dp[i - c]])
        return dp[target]

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_combinationSum2(self) -> None:
        sol = Solution()
        for candidates, target, solution in (
                [[2,3,6,7], 7, [[2,2,3],[7]]],
                [[2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]],
                [[2], 1, []],
                [[1], 1, [[1]]]
        ):
            self.assertEqual(solution, sol.combinationSum(candidates, target))
            self.assertEqual(solution, sol.combinationSum_using_DP(candidates, target))

if __name__ == "__main__":
    unittest.main()

