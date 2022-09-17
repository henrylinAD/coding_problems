# 0-1 Knapsack
# https://algo.monster/problems/knapsack_intro

# We want to discuss a classic dynamic programming problem, which is 0-1 knapsack. Given a series of objects with a
# weight and a value and a knapsack that can carry a set amount of weight, what is the maximum object value we can
# put in our knapsack without exceeding the weight constraint?
#
# Input
#   weights: an array of integers that denote the weights of objects
#   values: an array of integers that denote the values of objects
#   max_weight: the maximum weight capacity of the knapsack
# Output
# the maximum value in the knapsack
#
# Examples
# Example 1:
# Input:
#   1. weights = [3, 4, 7]
#   2. values = [4, 5, 8]
#   3. max_weight = 7
# Output: 9
#
# Explanation:
# We have a knapsack of max limit 7 with 3 objects of weight-value pairs of [3,4], [4,5], [7,8], then the maximal
# value we can achieve is using the first 2 objects to obtain value 4 + 5 = 9.
#
# The other possibilities would all be only 1 object in our knapsack, which would only yield values 4, 5, and 9.

# Solution
# Brute Force | DFS | Combinatorial Search
# A brute force method would enumerate all the possibilities such that for every object we try including it into our
# knapsack which would result in time complexity O(2^n) where n is the total number of objects. This can be done with
# a recursive combinatorial search where, for every item, we either choose to include it or not, then checking which
# possibility results in the greatest value while not exceeding the maximum weight.

# Note that the largest value while not exceeding the maximum weight is 9.
# helper function that returns the maximum value when considering
# the first n items and remaining available weight remaining_weight
def knapsack_helper(weights: List[int], values: List[int], remaining_weight: int, n: int) -> int:
    # base case: if there are no items or no available weight in the knapsack to use, the maximum value is 0
    if n == 0 or remaining_weight == 0:
        return 0
    # if the weight of the current item exceeds the available weight,
    # skip the current item and process the next one
    if weights[n - 1] > remaining_weight:
        return knapsack_helper(weights, values, remaining_weight, n - 1)
    # recurrence relation: choose the maximum of two possibilities:
    #   (1) pick up the current item: current value + maximum value with the rest of the items
    #   (2) give up the current item: maximum value with the rest of the items
    return max(values[n - 1] + knapsack_helper(weights, values, remaining_weight - weights[n - 1], n - 1),
               knapsack_helper(weights, values, remaining_weight, n - 1))


def knapsack(weights: List[int], values: List[int], max_weight: int) -> int:
    n = len(weights)
    return knapsack_helper(weights, values, max_weight, n)
