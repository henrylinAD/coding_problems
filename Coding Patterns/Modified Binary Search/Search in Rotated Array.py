# Problem Challenge 2: Search in Rotated Array (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744196413_85Unit

# Problem Statement
#
# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number,
# find if a given ‘key’ is present in it.
#
# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You
# can assume that the given array does not have any duplicates.
#
# Example 1:
# Input: [10, 15, 1, 3, 8], key = 15
# Output: 1
# Explanation: '15' is present in the array at index '1'.
#           Original array:     1   |   3   |   8   |   10   |   15   |
#  Array after 2 rotations:     10  |   15  |   1   |   3    |   8    |
#

# Example 2:
#
# Input: [4, 5, 7, 9, 10, -1, 2], key = 10
# Output: 4
# Explanation: '10' is present in the array at index '4'.
#           Original array:     -1   |   2   |   4   |   5   |   7   |   9   |   10   |
#  Array after 2 rotations:      4   |   5   |   7   |   9   |   10  |  -1   |    2   |

