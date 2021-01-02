# I. HashTable based technique:

> > Array is one of the fundamental blocks in algorithms. 
> > Since a string is just formed by an array of characters, they are similar. 
> > Most interview questions fall into this category.
> > Here we will discuss some common techniques to help you
> > solve these problems.

Whenever we see a problem of finding sub-array of sum `k`.

We need to immediately think of the following two ways to solve it:

1. Method 1: Brute-Force ( Every sub-array )       => TC: O(N^2) ; SC: O(1)
1. Method 2: HashTable                            => TC: O(N)   ; SC: O(N)

**NOTE:** For any sub-array problems, we need to instantly realize that indexes/positions/order
of the elements are important. Hence, we cannot sort, which would disrupt the order of the elements

> HashTable (or, Dictionary) can solve any two-sum problem without using the condition of a sorted array.

A classic example is to return ___indices of the two numbers such that they add up to___ `target`, 
given an array of integers `nums` and an integer `target`, i.e. the **Two-Sum Problem**,
which is available for you to practice here - [LeetCode - Problem 1 - Two Sum](https://leetcode.com/problems/two-sum/).

* **Using Method 1 - Brute Force**, nested loop get all combination of two numbers.
Because there is only n * (n - 1) / 2 combinations, the **Time Complexity** is `O(N^2)`.
We occupy no extra space in memory, so the **Space Complexity** is `O(1)`.

```python
from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        for i in range(len(nums) - 1):
            firstNum = nums[i]
            for j in range(i+1, len(nums)):
                secondNum = nums[j]
                if firstNum + secondNum == target:
                    return [i, j]
        return []
```

* **Using Method 2 - HashTable**, one pass, store and find target - nums[i] same time, 
the **Time Complexity** is `O(N)`, and, the **Space Complexity** is `O(N)`.

```python
from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        checker = {}
        for i, num in enumerate(nums):
            if target - num in checker:
                return [checker[target - num], i]
            checker[num] = i
        return []
```

The above approach is LBYL ( <ins>L</ins>ook <ins>B</ins>efore <ins>Y</ins>out <ins>L</ins>eap ) - the more pythonic way - of doing the
above is EAFP ( <ins>E</ins>asier to <ins>A</ins>sk for <ins>F</ins>orgiveness than <ins>P</ins>ermission ) [PEP 8](https://www.python.org/dev/peps/pep-0008/),
as shown below:

```python
from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        checker = {}
        for i, num in enumerate(nums):
            try:
                return [checker[num], i]
            except KeyError:
                checker[target - num] = i
        return []
```

#### **Classic problems that can be solved using this technique:**

1. [LeetCode - Problem 1 - Two Sum](https://leetcode.com/problems/two-sum)
1. [LeetCode - Problem 3 - Longest Substring Without Repeated Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
1. [LeetCode - Problem 18 - 4Sum](https://leetcode.com/problems/4sum)
1. [LeetCode - Problem 30 - Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words)
1. [LeetCode - Problem 36 - Valid Sudoku](https://leetcode.com/problems/valid-sudoku)
1. [LeetCode - Problem 37 - Sudoku Solver](https://leetcode.com/problems/sudoku-solver)
1. [LeetCode - Problem 49 - Group Anagrams](https://leetcode.com/problems/group-anagrams)
1. [LeetCode - Problem 76 - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)
1. [LeetCode - Problem 85 - Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle)
1. [LeetCode - Problem 94 - Binary Tree Inorder Traversal](https://leetcode.com/problems/maximal-rectangle)
1. [LeetCode - Problem 136 - Single Number]
1. [LeetCode - Problem 138 - Copy List with Random Pointer]	
1. [LeetCode - Problem 149 -  Max Points on a Line]	
1. [LeetCode - Problem 159 - Longest Substring with At Most Two Distinct Characters]
1. [LeetCode - Problem 166 - Fraction to Recurring Decimal]	
1. [LeetCode - Problem 170 - Two Sum III]
1. [LeetCode - Problem 187 - Repeated DNA Sequences]	
1. [LeetCode - Problem 202 - Happy Number]	
1. [LeetCode - Problem 204 - Count Primes]	
1. [LeetCode - Problem 205 - Isomorphic Strings]	
1. [LeetCode - Problem 217 - Contains Duplicate]	
1. [LeetCode - Problem 219 - Contains Duplicate II]	
1. [LeetCode - Problem 242 - Valid Anagram]
1. [LeetCode - Problem 244 - Shortest Word Distance II]
1. [LeetCode - Problem 246 - Strobogrammatic Number]
1. [LeetCode - Problem 249 - Group Shifted Strings]
1. [LeetCode - Problem 266 - Palindrome Permutation]
1. [LeetCode - Problem 274 - H-Index]	
1. [LeetCode - Problem 288 - Unique Word Abbreviation]
1. [LeetCode - Problem 290 - Word Pattern]	
1. [LeetCode - Problem 299 - Bulls and Cows]	
1. [LeetCode - Problem 311 - Sparse Matrix Multiplication]
1. [LeetCode - Problem 325 - Maximum Size Subarray Sum Equals k]
1. [LeetCode - Problem 336 - Palindrome Pairs]
1. [LeetCode - Problem 340 - Longest Substring with At Most K Distinct Characters]
1. [LeetCode - Problem 347 - Top K Frequent Elements]
1. [LeetCode - Problem 349 - Intersection of Two Arrays]
1. [LeetCode - Problem 350 - Intersection of Two Arrays II]
1. [LeetCode - Problem 355 - Design Twitter]
1. [LeetCode - Problem 356 - Line Reflection]
1. [LeetCode - Problem 358 - Rearrange String k Distance Apart]
1. [LeetCode - Problem 359 - Logger Rate Limiter]
1. [LeetCode - Problem 380 - Insert Delete GetRandom O(1)]
1. [LeetCode - Problem 381 - Insert Delete GetRandom O(1) - Duplicates allowed]
1. [LeetCode - Problem 387 - First Unique Character in a String]
1. [LeetCode - Problem 389 - Find the Difference]
1. [LeetCode - Problem 409 - Longest Palindrome]
1. [LeetCode - Problem 438 - Find All Anagrams in a String]
1. [LeetCode - Problem 447 - Number of Boomerangs]
1. [LeetCode - Problem 451 - Sort Characters By Frequency]
1. [LeetCode - Problem 454 - 4Sum II]
1. [LeetCode - Problem 463 - Island Perimeter]
1. [LeetCode - Problem 500 - Keyboard Row]
1. [LeetCode - Problem 508 - Most Frequent Subtree Sum]
1. [LeetCode - Problem 525 - Contiguous Array]
1. [LeetCode - Problem 535 - Encode and Decode TinyURL]
1. [LeetCode - Problem 554 - Brick Wall]
1. [LeetCode - Problem 560 - Subarray Sum Equals K]	
1. [LeetCode - Problem 575 - Distribute Candies]
1. [LeetCode - Problem 594 - Longest Harmonious Subsequence]	
1. [LeetCode - Problem 599 - Minimum Index Sum of Two Lists]	
1. [LeetCode - Problem 609 - Find Duplicate File in System]	
1. [LeetCode - Problem 624 - Maximum Distance in Arrays]
1. [LeetCode - Problem 632 - Smallest Range Covering Elements from K Lists]
1. [LeetCode - Problem 645 - Set Mismatch]
1. [LeetCode - Problem 648 - Replace Words]
1. [LeetCode - Problem 676 - Implement Magic Dictionary]
1. [LeetCode - Problem 690 - Employee Importance]
1. [LeetCode - Problem 692 - Top K Frequent Words]
1. [LeetCode - Problem 694 - Number of Distinct Islands]
1. [LeetCode - Problem 711 - Number of Distinct Islands II]
1. [LeetCode - Problem 718 - Maximum Length of Repeated Subarray]	
1. [LeetCode - Problem 720 - Longest Word in Dictionary]	
1. [LeetCode - Problem 726 - Number of Atoms]
1. [LeetCode - Problem 734 - Sentence Similarity]
1. [LeetCode - Problem 739 - Daily Temperatures]	
1. [LeetCode - Problem 748 - Shortest Completing Word]
1. [LeetCode - Problem 760 - Find Anagram Mappings]
1. [LeetCode - Problem 770 - Basic Calculator IV]	
1. [LeetCode - Problem 771 - Jewels and Stones]	
1. [LeetCode - Problem 781 - Rabbits in Forest]	
1. [LeetCode - Problem 705 - Design HashSet]	
1. [LeetCode - Problem 706 - Design HashMap]	
1. [LeetCode - Problem 811 - Subdomain Visit Count]	
1. [LeetCode - Problem 710 - Random Pick with Blacklist]	
1. [LeetCode - Problem 884 - Uncommon Words from Two Sentences]	
1. [LeetCode - Problem 895 - Maximum Frequency Stack]	
1. [LeetCode - Problem 930 - Binary Subarrays With Sum]	
1. [LeetCode - Problem 939 - Minimum Area Rectangle]	
1. [LeetCode - Problem 953 - Verifying an Alien Dictionary]	
1. [LeetCode - Problem 954 - Array of Doubled Pairs]	
1. [LeetCode - Problem 957 - Prison Cells After N Days]	
1. [LeetCode - Problem 961 - N-Repeated Element in Size 2N Array]	
1. [LeetCode - Problem 966 - Vowel Spellchecker]	
1. [LeetCode - Problem 970 - Powerful Integers]	
1. [LeetCode - Problem 974 - Subarray Sums Divisible by K]	
1. [LeetCode - Problem 981 - Time Based Key-Value Store]	
1. [LeetCode - Problem 987 - Vertical Order Traversal of a Binary Tree]	
1. [LeetCode - Problem 992 - Subarrays with K Different Integers]	
1. [LeetCode - Problem 1001 - Grid Illumination]	
1. [LeetCode - Problem 1002 - Find Common Characters]	
1. [LeetCode - Problem 1086 - High Five]
1. [LeetCode - Problem 1133 - Largest Unique Number]
1. [LeetCode - Problem 1152 - Analyze User Website Visit Pattern]
1. [LeetCode - Problem 1160 - Find Words That Can Be Formed by Characters]	
1. [LeetCode - Problem 1044 - Longest Duplicate Substring]	
1. [LeetCode - Problem 1166 - Design File System]
1. [LeetCode - Problem 1048 - Longest String Chain]	
1. [LeetCode - Problem 1198 - Find Smallest Common Element in All Rows]
1. [LeetCode - Problem 1072 - Flip Columns For Maximum Number of Equal Rows]	
1. [LeetCode - Problem 1213 - Intersection of Three Sorted Arrays]
1. [LeetCode - Problem 1078 - Occurrences After Bigram]	
1. [LeetCode - Problem 1090 - Largest Values From Labels]	
1. [LeetCode - Problem 1244 - Design A Leaderboard]
1. [LeetCode - Problem 1138 - Alphabet Board Path]	
1. [LeetCode - Problem 1178 - Number of Valid Words for Each Puzzle]	
1. [LeetCode - Problem 1189 - Maximum Number of Balloons]	
1. [LeetCode - Problem 1207 - Unique Number of Occurrences]	
1. [LeetCode - Problem 1224 - Maximum Equal Frequency]
1. [LeetCode - Problem 1429 - First Unique Number]
1. [LeetCode - Problem 1261 - Find Elements in a Contaminated Binary Tree]	
1. [LeetCode - Problem 1311 - Get Watched Videos by Your Friends]	
1. [LeetCode - Problem 1365 - How Many Numbers Are Smaller Than the Current Number]	
1. [LeetCode - Problem 1418 - Display Table of Food Orders in a Restaurant]	
1. [LeetCode - Problem 1487 - Making File Names Unique]	
1. [LeetCode - Problem 1488 - Avoid Flood in The City]	
1. [LeetCode - Problem 1485 - Clone Binary Tree With Random Pointer]
1. [LeetCode - Problem 1490 - Clone N-ary Tree]
1. [LeetCode - Problem 1512 - Number of Good Pairs]	
1. [LeetCode - Problem 1539 - Kth Missing Positive Number]	
1. [LeetCode - Problem 1590 - Make Sum Divisible by P]	
1. [LeetCode - Problem 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers]	
1. [LeetCode - Problem 1570 - Dot Product of Two Sparse Vectors]
1. [LeetCode - Problem 1638 - Count Substrings That Differ by One Character]	
1. [LeetCode - Problem 1612 - Check If Two Expression Trees are Equivalent]
1. [LeetCode - Problem 1679 - Max Number of K-Sum Pairs]
