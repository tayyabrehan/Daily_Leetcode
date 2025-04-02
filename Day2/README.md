# 2873. Maximum Value of an Ordered Triplet I

## Problem Description
You are given a 0-indexed integer array `nums`.

Return the maximum value over all triplets of indices `(i, j, k)` such that `i < j < k`. If all such triplets have a negative value, return `0`.

The value of a triplet `(i, j, k)` is calculated as `(nums[i] - nums[j]) * nums[k]`.

### Examples
**Example 1:**  
Input: `nums = [12,6,1,2,7]`  
Output: `77`  
Explanation: The value of triplet `(0, 2, 4)` is `(12 - 1) * 7 = 77`.

**Example 2:**  
Input: `nums = [1,10,3,4,19]`  
Output: `133`  
Explanation: The value of triplet `(1, 2, 4)` is `(10 - 3) * 19 = 133`.

**Example 3:**  
Input: `nums = [1,2,3]`  
Output: `0`  
Explanation: The only triplet `(0, 1, 2)` gives `(1 - 2) * 3 = -3` (negative), so return `0`.

## Constraints
- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 10^6`