# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

# solution #1
# def longestCommonPrefix(strs):
#
#     if not strs:
#         return ""
#
#     for i in range(len(strs[0])):
#         for string in strs[1:]:
#             if i >= len(string) or string[i] != strs[0][i]:
#                 return strs[0][:i]
#
#     return strs[0] # strs[0] == ""; string exist as empty str("")

def longestCommonPrefix(strs):
