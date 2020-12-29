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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(curr, idx):
            if sum(curr) > target:
                return
            if sum(curr) == target:
                res.append(curr)
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                dfs(curr + [candidates[i]], i + 1)

        dfs([], 0)

        return res

    # Solution 1 : DP solution
    #
    # TC: O(K*log(K))
    #
    def combinationSum2_using_DP(self, candidates: List[int], target: int) -> List[List[int]]:
        # dp = [set([()])] + [set([]) for i in range(target)]
        # for c in sorted(candidates):
        #     for n in range(target, c - 1, -1):
        #         dp[n] |= {t + (c,) for t in dp[n - c]}
        # res = [list(t) for t in dp[target]]
        # res.sort()
        # return res
        counter = collections.Counter(candidates)
        dp = [[[]]] + [[] for _ in range(target + 1)]
        for c, cnt in counter.items():
            for i in range(c, target + 1):
                dp[i].extend([arr + [c] for arr in dp[i - c] if len(arr) < cnt or arr[-cnt] != c])
        res = dp[target]
        res.sort()
        return res

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_combinationSum2(self) -> None:
        sol = Solution()
        for candidates, target, solution in (
                [[10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]],
                [[2,5,2,1,2], 5, [[1,2,2],[5]]]
        ):
            self.assertEqual(solution, sol.combinationSum2(candidates, target))
            self.assertEqual(solution, sol.combinationSum2_using_DP(candidates, target))

if __name__ == "__main__":
    unittest.main()

