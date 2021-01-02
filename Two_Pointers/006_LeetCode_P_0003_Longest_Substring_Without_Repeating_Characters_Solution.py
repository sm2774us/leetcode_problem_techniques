# LeetCode - Problem 3 - Longest Substring Without Repeating Characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
#
from typing import List
from math import inf

import unittest

class Solution:
    # Solution : Two-Pointers Technique
    #
    #            This solution uses a "sliding window" hash set.
    #
    # Detailed explanation:
    #
    # `left` and `right` are indexes into the string.
    # These bound the current substring we're looking at. We also have a hash set, chars,
    # which stores the characters in the current substring.
    #
    # Both indices start at 0. We check if string[right] is in our hash set of current characters;
    # if it isn't, it's a unique character we can add to the current substring. So, we add it to the set of characters,
    # and increment right. We also potentially update longest with the length of the current substring.
    #
    # If string[right] is in the hash set of characters, we remove string[left] from the hash set, and increment left.
    # This is because the character at right is a duplicate of some character in the substring;
    # we want to keep removing the leftmost character from the current substring until we remove that character.
    # Then, since we have another candidate for longest non-repeating substring, we can enter the if block,
    # and go back to incrementing right.
    #
    # By the time the while loop terminates, we've considered every substring with unique characters,
    # and we know the length of the longest. left and right were incremented linearly through the string,
    # and the hash set allowed for O(1) lookups, so the time complexity is O(n).
    #
    # TC: O(N)
    # SC: O(K)
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time:  O(n)
        Space: O(k)
        [k = length of the longest substring w/o repeating characters]
        """
        if not s: return 0
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(s) and right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(s[left])
                left += 1
        return longest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_lengthOfLongestSubstring(self) -> None:
        sol = Solution()
        for s, solution in (
            ["abcabcbb", 3],          # The answer is "abc", with the length of 3.
            ["bbbbb", 1],
            ["pwwkew", 3],
            ["", 0]
        ):
            self.assertEqual(solution, sol.lengthOfLongestSubstring(s))

if __name__ == "__main__":
    unittest.main()
