# Remove Duplicates (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743424499_2Unit

# Problem Statement
#
# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element
# appears only once. The relative order of the elements should be kept the same and you should not use any extra
# space so that the solution have a space complexity of O(1).
#
# Move all the unique elements at the beginning of the array and after moving return the length of the subarray that
# has no duplicate in it.
#
# Example 1:
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
#
# Example 2:
# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

# Solution
#
# In this problem, we need to separate the duplicates in-place such that the resultant length of the array remains
# sorted. As the input array is sorted, therefore, one way to do this is to shift the elements left whenever we
# encounter duplicates. In other words, we will keep one pointer for iterating the array and one pointer for placing
# the next non-duplicate number. So our algorithm will be to iterate the array and whenever we see a non-duplicate
# number we move it next to the last non-duplicate number we’ve seen.
