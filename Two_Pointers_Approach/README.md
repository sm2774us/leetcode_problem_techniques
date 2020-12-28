# I. Two-pointer technique:

> > Array is one of the fundamental blocks in algorithms. 
> > Since a string is just formed by an array of characters, they are similar. 
> > Most interview questions fall into this category.
> > Here we will discuss some common techniques to help you
> > solve these problems.

These kind of problems usually involve two pointers:

> One slow-runner and the other fast-runner.

A classic example is to remove duplicates from a sorted array,
which is available for you to practice here - [LeetCode - Problem 26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/).

> One pointer starts from the beginning while the other pointer starts from the end.

They move toward each other until they both meet. Let's take a look at a classic problem: Reverse the characters in a string:

First let's assume we already have a `swap` function as defined below:

```python
from typing import List

class Solution:
    
    def swap(self, s: List[str], i: int, j: int) -> None:
        s[i], s[j] = s[j], s[i]
```

The idea is to swap the first character with the end,
advance to the next character and swapping repeatedly until
it reaches the middle position. We calculate the middle position
as ![equation](http://latex.codecogs.com/svg.latex?%5Cleft%20%5Clfloor%20%5Cfrac%7Bn%7D%7B2%7D%20%5Cright%20%5Crfloor).
You should verify that the middle position works for both odd and even
size of array.

```python
from typing import List

class Solution:
    
    def swap(self, s: List[str], i: int, j: int) -> None:
        s[i], s[j] = s[j], s[i]

    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(0,(n//2)):
            self.swap(s,i,n-i-1)
```

Or we can solve the problem using the two-pointer technique:

```python
from typing import List

class Solution:
    
    def swap(self, s: List[str], i: int, j: int) -> None:
        s[i], s[j] = s[j], s[i]

    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s)-1
        while i < j:
            self.swap(s, i, j)
            i += 1
            j -= 1
```

Which approach do you think is less likely to introduce bugs?

#### **Classic problems that can be solved using this technique:**

1. [LeetCode - Problem 1 - Two Sum](https://leetcode.com/problems/two-sum/)
1. [LeetCode - Problem 167 - Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
1. [LeetCode - Problem 3 - Longest Substring Without Repeated Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
1. [LeetCode - Problem 11 - Container With Most Water](https://leetcode.com/problems/container-with-most-water/).
1. [LeetCode - Problem 15 - 3Sum]
1. [LeetCode - Problem 16 - 3Sum Closest]
1. [LeetCode - Problem 18 - 4Sum]
1. [LeetCode - Problem 19 - Remove Nth Node From End of List]
1. [LeetCode - Problem 26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/).
1. [LeetCode - Problem 27 - Remove Element]
1. [LeetCode - Problem 28 - Implement `strStr()`]
1. [LeetCode - Problem 30 - Substring with Concatenation of All Words]
1. [LeetCode - Problem 42 - Trapping Rain Water]
1. [LeetCode - Problem 61 - Rotate List]
1. [LeetCode - Problem 75 - Sort Colors]
1. [LeetCode - Problem 76 - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)   
1. [LeetCode - Problem 80 - Remove Duplicates from Sorted Array II]
1. [LeetCode - Problem 86 - Partition List]
1. [LeetCode - Problem 88 - Merge Sorted Array] 
1. [LeetCode - Problem 125 - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/).
1. [LeetCode - Problem 141 - Linked List Cycle]
1. [LeetCode - Problem 159 - Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
1. [LeetCode - Problem 167 - Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/).
1. [LeetCode - Problem 186 - Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/).
1. [LeetCode - Problem 189 - Rotate Array](https://leetcode.com/problems/rotate-array/).
1. [LeetCode - Problem 209 - Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
1. [LeetCode - Problem 234 - Palindrom Linked List]
1. [LeetCode - Problem 238 - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/).
1. [LeetCode - Problem 259 - 3Sum Smaller]
1. [LeetCode - Problem 283 - Move Zeroes]
1. [LeetCode - Problem 287 - Find the Duplicate Number]
1. [LeetCode - Problem 340 - Longest Substring with At Most K Distinct Characters]
1. [LeetCode - Problem 344 - Reverse String]
1. [LeetCode - Problem 345 - Reverse Vowels of a String]
1. [LeetCode - Problem 349 - Intersection of Two Arrays]
1. [LeetCode - Problem 350 - Intersection of Two Arrays II]
1. [LeetCode - Problem 360 - Sort Transformed Array]
1. [LeetCode - Problem 424 - Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
1. [LeetCode - Problem 457 - Circular Array Loop]
1. [LeetCode - Problem 487 - Maximum Consecutive Ones II]
1. [LeetCode - Problem 524 - Longest Word in Dictionary through Deleting]
1. [LeetCode - Problem 532 - K-diff Pairs in an Array]
1. [LeetCode - Problem 567 - Permutation in String]
1. [LeetCode - Problem 632 - Smallest Range Covering Elements from K Lists]
1. [LeetCode - Problem 713 - Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
1. [LeetCode - Problem 763 - Partition Labels]
1. [LeetCode - Problem 826 - Most Profit Assigning Work]
1. [LeetCode - Problem 828 - Count Unique Characters of All Substrings of a Given String]
1. [LeetCode - Problem 838 - Push Dominoes]
1. [LeetCode - Problem 844 - Backspace String Compare]
1. [LeetCode - Problem 845 - Longest Mountain in Array]
1. [LeetCode - Problem 881 - Boats to Save People]
1. [LeetCode - Problem 904 - Fruit into Baskets]
1. [LeetCode - Problem 923 - 3Sum with Multiplicity]
1. [LeetCode - Problem 925 - Long Pressed Name]
1. [LeetCode - Problem 930 - Binary Subarrays With Sum]
1. [LeetCode - Problem 948 - Bag of Tokens]
1. [LeetCode - Problem 977 - Squares of a Sorted Array]
1. [LeetCode - Problem 986 - Interval List Intersections]
1. [LeetCode - Problem 992 - Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)
1. [LeetCode - Problem 1004 - Max Consecutive Ones III]
1. [LeetCode - Problem 1099 - Two Sum Less Than K]
1. [LeetCode - Problem 1208 - Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/)
1. [LeetCode - Problem 1213 - Intersection of Three Sorted Arrays]
1. [LeetCode - Problem 1093 - Statistics from a Large Sample]
1. [LeetCode - Problem 1234 - Replace the Substring for Balanced String]
1. [LeetCode - Problem 1248 - Count Number of Nice Subarrays]
1. [LeetCode - Problem 1570 - Dot Product of Two Sparse Vectors]
1. [LeetCode - Problem 1610 - Maximum Number of Visible Points]
1. [LeetCode - Problem 1616 - Split Two Strings to Make Palindrome]
1. [LeetCode - Problem 1658 - Minimum Operations to Reduce X to Zero]
1. [LeetCode - Problem 1687 - Delivering Boxes from Storage to Ports]
1. [LeetCode - Problem 1695 - Maximum Erasure Value]
