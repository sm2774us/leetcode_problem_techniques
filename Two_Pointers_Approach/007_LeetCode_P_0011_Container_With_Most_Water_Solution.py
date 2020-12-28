# LeetCode - Problem 11 - Container With Most Water (https://leetcode.com/problems/container-with-most-water/)
#
from typing import List
from math import inf

import unittest

class Solution:
    # Solution : Two-Pointer Approach
    #
    # Algorithm:
    # ----------------------
    # The intuition behind this approach is that the area formed between the lines
    # will always be limited by the height of the shorter line. Further, the farther the lines,
    # the more will be the area obtained.
    #
    # We take two pointers, one at the beginning and one at the end of the array
    # constituting the length of the lines. Futher, we maintain a variable `maxarea` to store the
    # maximum area obtained till now. At every step, we find out the area formed between them,
    # update `maxarea` and move the pointer pointing to the shorter line towards the other end by one step.
    #
    # How this approach works?
    #
    # Initially we consider the area constituting the exterior most lines.
    # Now, to maximize the area, we need to consider the area between the lines of larger lengths.
    # If we try to move the pointer at the longer line inwards, we won't gain any increase in area,
    # since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial,
    # as per the same argument, despite the reduction in the width.
    # This is done since a relatively longer line obtained by moving the shorter line's pointer
    # might overcome the reduction in area caused by the width reduction.
    # ----------------------
    # Further Clarification:
    # ----------------------
    # Here's another way to see what happens in a matrix representation:
    #
    # Draw a matrix where rows correspond to the position of the left line, and columns corresponds to the position of the right line.
    #
    # For example, say n=6. Element at (2,4) would corresponds to the case where the left line is at position 2 and the right line is at position 4. The value of the element is the volume for the case.
    #
    # In the figures below, x means we don't need to compute the volume for that case, because:
    #
    # on the diagonal, the two lines are overlapped;
    # the lower left triangle area of the matrix, the two lines are switched and the case is symmetric to the upper right area.
    # We start by computing the volume at (1,6), denoted by o. Now if the left line is shorter than the right line, then moving the right line towards left would only decrease the volume, so all the elements left to (1,6) on the first row have smaller volume. Therefore, we don't need to compute those cases (crossed by ---).
    #
    #   1 2 3 4 5 6
    # 1 x ------- o
    # 2 x x
    # 3 x x x
    # 4 x x x x
    # 5 x x x x x
    # 6 x x x x x x
    # So we can only move the left line towards right to 2 and compute (2,6). Now if the right line is shorter, all cases below (2,6) are eliminated.
    #
    #   1 2 3 4 5 6
    # 1 x ------- o
    # 2 x x       o
    # 3 x x x     |
    # 4 x x x x   |
    # 5 x x x x x |
    # 6 x x x x x x
    # And no matter how this o path goes, we end up only need to find the max value on this path, which contains n-1 cases.
    #
    #   1 2 3 4 5 6
    # 1 x ------- o
    # 2 x x - o o o
    # 3 x x x o | |
    # 4 x x x x | |
    # 5 x x x x x |
    # 6 x x x x x x
    #
    # Hope this helps. I feel more comfortable seeing things this way.
    # ----------------------
    # One thing that is ignored in the explanation is the h[i] == h[j] case.
    # You need to prove that in this case, it does not matter whether you perform i++ or j--,
    # because if h[i] == h[j], neither (i+1, j) or (i, j-1) can be potential solutions
    # because the area obtained is necessarily smaller than (i, j).
    # ----------------------
    # Explanation if h[i] == h[j] :
    # ----------------------
    # Let's consider the cases where we have h[i] == h[j].
    #
    # (The numbers denote the height of the container and the underscores denote a width of magnitude 1)
    #
    # Case 1: Between h[i] and h[j], we have both containers that have lengths smaller than h[i] or h[j], i.e.
    # something like 2_1_1_2 which can be generalized to 2_1......1_2.
    # In this case, either moving left or right won't help. If we move right, we have 1_1_2, or if we move left,
    # we have 2_1_1. In either case, our new area would be 2 sq units which is lesser
    # than the initial area of 6 sq units.
    #
    # Case 2: Between h[i] and h[j], we have both containers that have lengths greater than h[i] or h[j],
    # i.e. something like 2_3_3_2 which can be generalized to 2_3......3_2.
    # In this case, either moving left or right won't help. If we move right, we have 3_3_2,
    # or if we move left, we have 2_3_3. In either case, our new area would be 4 sq units which is lesser
    # than the initial area of 6 sq units. The new area would always be bounded by the smaller height
    # (which comes from h[i] or h[j])
    #
    # Case 3: Between h[i] and h[j], we have one container that has length greater than h[i]
    # and one container that has length smaller than h[j], i.e. something like 2_1_3_2
    # which can be generalized to 2_1......3_2 or vice versa. In this case, if we move right,
    # we have 1_3_2 where the new area would be 2 sq units. If we move left, we have 2_1_3,
    # where the new area would be 4 sq units. Again, in any case, our new area would always
    # be smaller than our initial area of 6 sq units.
    #
    #
    # ----------------------
    # Proof:
    # ----------------------
    # Here is the proof.
    # Proved by contradiction:
    #
    # Suppose the returned result is not the optimal solution. Then there must exist an optimal solution,
    # say a container with a_ol and a_or (left and right respectively), such that it has a greater volume
    # than the one we got. Since our algorithm stops only if the two pointers meet.
    # So, we must have visited one of them but not the other. WLOG, let's say we visited a_ol but not a_or.
    # When a pointer stops at a_ol, it won't move until
    #
    # The other pointer also points to a_ol.
    # In this case, iteration ends. But the other pointer must have visited a_or on its way from right end to a_ol.
    # Contradiction to our assumption that we didn't visit a_or.
    #
    # The other pointer arrives at a value, say a_rr, that is greater than a_ol before it reaches a_or.
    # In this case, we does move a_ol. But notice that the volume of a_ol and a_rr
    # is already greater than a_ol and a_or (as it is wider and heigher),
    # which means that a_ol and a_or is not the optimal solution -- Contradiction!
    #
    # Both cases arrive at a contradiction.
    # ----------------------
    # Complexity Analysis
    # ----------------------
    # Time complexity : O(n)O(n). Single pass.
    #
    # Space complexity : O(1)O(1). Constant space is used.
    #
    # ----------------------
    # Simplified Idea/Proof:
    # ----------------------
    # 1. The widest container (using first and last line) is a good candidate, because of its width.
    #    Its water level is the height of the smaller one of first and last line.
    # 2. All other containers are less wide and thus would need a higher water level in order to hold more water.
    # 3. The smaller one of first and last line doesn't support a higher water level
    #    and can thus be safely removed from further consideration.
    #
    # Further explanation:
    # ----------------------
    # Variables `left` and `right` define the container under consideration.
    # We initialize them to first and last line, meaning the widest container.
    # Variable `max_area` will keep track of the highest amount of water we managed so far.
    # We compute `right - left`, the width of the current container, and `min(height[left], height[right])`,
    # the water level that this container can support.
    # Multiply them to get how much water this container can hold, and update water accordingly.
    # Next remove the smaller one of the two lines from consideration, as justified above in "Idea / Proof".
    # Continue until there is nothing left to consider, then return the result.
    #
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            if height[left] >= height[right]:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1
            else:
                max_area = max(max_area, height[left] * (right - left))
                left += 1

        return max_area


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxArea(self) -> None:
        sol = Solution()
        #
        # 8 |-        +--+                          +--+
        # 7 |-        |  |xxxxxxxxxxxxxxxxxxxxxxxxxx|  |xxxxxxxx+--+
        # 6 |-        |  |xx+--+xxxxxxxxxxxxxxxxxxxx|  |xxxxxxxx|  |
        # 5 |-        |  |xx|  |xxxxxxxx+--+xxxxxxxx|  |xxxxxxxx|  |
        # 4 |-        |  |xx|  |xxxxxxxx|  |xx+--+xx|  |xxxxxxxx|  |
        # 3 |-        |  |xx|  |xxxxxxxx|  |xx|  |xx|  |xx+--+xx|  |
        # 2 |-        |  |xx|  |xx+--+xx|  |xx|  |xx|  |xx|  |xx|  |
        # 1 |-  +--+  |  |xx|  |xx|  |xx|  |xx|  |xx|  |xx|  |xx|  |
        # 0 +---+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--
        for height, solution in (
            [[1,8,6,2,5,4,8,3,7], 49],      # The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
                                            # In this case, the max area of water (blue section) the container can contain is 49.
                                            # The answer is "abc", with the length of 3.
            [[1, 1], 1],
            [[4,3,2,1,4], 16],
            [[1,2,1], 2]
        ):
            self.assertEqual(solution, sol.maxArea(height))

if __name__ == "__main__":
    unittest.main()
