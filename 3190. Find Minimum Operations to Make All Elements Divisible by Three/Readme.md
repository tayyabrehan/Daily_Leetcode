# 3190. Find Minimum Operations to Make All Elements Divisible by Three

## Problem Description
You are given an integer array `nums`. In one operation, you can add or subtract 1 from **any** element of `nums`.

Return the **minimum** number of operations to make all elements of `nums` divisible by 3.



## Examples

### Example 1:
**Input:** `nums = [1,2,3,4]`  
**Output:** `3`  
**Explanation:** All array elements can be made divisible by 3 using 3 operations:  
- Subtract 1 from 1 ($1 - 1 = 0$, $0$ is divisible by 3).  
- Add 1 to 2 ($2 + 1 = 3$, $3$ is divisible by 3).  
- Subtract 1 from 4 ($4 - 1 = 3$, $3$ is divisible by 3).  
The element 3 is already divisible by 3.

### Example 2:
**Input:** `nums = [3,6,9]`  
**Output:** `0`  
**Explanation:** All elements in the array are already divisible by 3.

## Constraints:
* `1 <= nums.length <= 50`
* `1 <= nums[i] <= 50`