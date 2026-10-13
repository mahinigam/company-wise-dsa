"""Find the Duplicate Number

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/find-the-duplicate-number/

Problem summary: Find the duplicate in n+1 integers constrained to 1..n without modifying the array.
Approach: Treat nums[value] as a linked-list pointer and use Floyd cycle detection.
Complexity: O(n) time and O(1) space.
"""

def find_duplicate(nums: list[int]) -> int:
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]; fast = nums[fast]
    return slow

assert find_duplicate([1,3,4,2,2]) == 2
assert find_duplicate([3,1,3,4,2]) == 3
assert find_duplicate([1,1]) == 1
