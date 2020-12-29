# LeetCode - Problem 923 - 3Sum With Multiplicity (https://leetcode.com/problems/3sum-with-multiplicity/)
#
from typing import List
import collections
import itertools
import operator
import math

import unittest

class Solution:
    # Solution : Two-Pointers Technique
    #
    # TC: O(N + M^2)
    # SC: O(M)
    #
    # where: `n` is the length of the input array.
    #        `m` is the number of distinct elements in the input array.
    def threeSumMulti(self, A: List[int], target: int) -> int:
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        bound = 1000000007
        dic = collections.Counter(A)
        A = sorted(dic.items(), key = lambda x: x[0])
        res = 0
        for i in range(len(A)):
            j = i
            k = len(A)-1
            new_target = target - A[i][0]
            while j <= k:
                if A[j][0]+A[k][0] < new_target:
                    j += 1
                elif A[j][0]+A[k][0] > new_target:
                    k -= 1
                else:
                    if A[i][0] == A[k][0]:
                        res = (res + A[i][1]*(A[i][1]-1)*(A[i][1]-2) // 6) % bound
                    elif A[i][0] == A[j][0]:
                        res = (res + A[k][1]*A[i][1]*(A[i][1]-1)//2) % bound
                    elif A[j][0] == A[k][0]:
                        res = (res + A[i][1]*A[j][1]*(A[j][1]-1)//2) % bound
                    else:
                        res = (res + A[i][1]*A[j][1]*A[k][1]) % bound
                    j += 1
                    k -= 1
        return res

    #
    # DP Solution
    #
    # - Let d1 track the count of single elements seen so far
    # - Let d2 track the count of the sum of any two elements seen so far
    # - Given a new value n, the number of 3-sums equal to target is d2[target-n]
    # - update d2, then d1
    #
    def threeSumMulti_using_DP(self, A: List[int], target: int) -> int:
        # https://www.hackerearth.com/practice/notes/abhinav92003/why-output-the-answer-modulo-109-7/
        # explanation of why a MOD is necessary when computing size of permutation of array which is n!
        MOD = (10 ** 9) + 7

        # track individual digits and number of occurences
        single_num_count = collections.defaultdict(int)

        # track sum of two numbers and numbers of occurences
        pair_sum_count = collections.defaultdict(int)
        output = 0

        for i in range(len(A)):
            curr_num = A[i]

            # add complements(pair) to output
            output += pair_sum_count[target - curr_num]

            # see note above for MOD
            output %= MOD

            # skips first iteration since no pairs yet
            for single_num, count in single_num_count.items():
                # add seen pair and number of occurrences
                pair_sum_count[curr_num + single_num] += count

            single_num_count[curr_num] += 1

        return output

    def threeSumMulti_using_python_3_reduce(self, A: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        c = collections.Counter(A)
        A = sorted(c.keys())
        ans = 0
        for k in range(len(A) - 1, -1, -1):
            for j in range(k, -1, -1):
                if (Ai := target - A[k] - A[j]) >= 0 and Ai in c and Ai <= A[j] <= A[k]:
                    cc = collections.Counter((Ai, A[j], A[k]))
                    ans += itertools.reduce(operator.mul, (math.comb(c[n], v) for n, v in cc.items())) % mod
        return ans % mod

    #
    # Solution using built-in - itertools.combinations_with_replacement(...)
    #
    # Count the occurrence of each number.
    # using hashmap or array up to you.
    #
    # Loop i on all numbers,
    # loop j on all numbers,
    # check if k = target - i - j is valid.
    #
    # Add the number of this combination to result.
    # 3 cases covers all possible combination:
    #
    # i == j == k
    # i == j != k
    # i < k && j < k
    # Time Complexity:
    # 3 <= A.length <= 3000, so N = 3000
    # But 0 <= A[i] <= 100
    # So my solution is O(N + 101 * 101)
    #
    # TC: O(N + 101*101)
    def threeSumMulti_using_itertools_combinations_with_replacement(self, A: List[int], target: int) -> int:
        c = collections.Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: res += c[i] * (c[i] - 1) * (c[i] - 2) / 6
            elif i == j != k: res += c[i] * (c[i] - 1) / 2 * c[k]
            elif k > i and k > j: res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_threeSumMulti(self) -> None:
        sol = Solution()
        for nums, target, solution in (
            [[1,1,2,2,3,3,4,4,5,5], 8, 20],            # Enumerating by the values (A[i], A[j], A[k]):
                                                       # (1, 2, 5) occurs 8 times;
                                                       # (1, 3, 4) occurs 8 times;
                                                       # (2, 2, 4) occurs 2 times;
                                                       # (2, 3, 3) occurs 2 times.
            [[1,1,2,2,2,2], 5, 12]
        ):
            self.assertEqual(solution, sol.threeSumMulti(nums, target))
            self.assertEqual(solution, sol.threeSumMulti_using_DP(nums, target))
            self.assertEqual(solution, sol.threeSumMulti_using_itertools_combinations_with_replacement(nums, target))

if __name__ == "__main__":
    unittest.main()
