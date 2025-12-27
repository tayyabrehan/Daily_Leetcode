# 2769. Find the Maximum Achievable Number

## Problem Description
Given two integers, `num` and `t`. A number `x` is **achievable** if it can become equal to `num` after applying the following operation at most `t` times:

* Increase or decrease `x` by **1**, and **simultaneously** increase or decrease `num` by **1**.

Return the **maximum** possible value of `x`.

## Examples

### Example 1:
**Input:** `num = 4`, `t = 1`  
**Output:** `6`  
**Explanation:** Apply the following operation once to make the maximum achievable number equal to `num`:  
* Decrease the maximum achievable number by 1 ($6 - 1 = 5$).  
* Increase `num` by 1 ($4 + 1 = 5$).  
Both numbers are now equal.

### Example 2:
**Input:** `num = 3`, `t = 2`  
**Output:** `7`  
**Explanation:** Apply the following operation twice to make the maximum achievable number equal to `num`:  
* Decrease the maximum achievable number by 1 twice ($7 - 1 - 1 = 5$).  
* Increase `num` by 1 twice ($3 + 1 + 1 = 5$).  
Both numbers are now equal.

## Constraints:
* `1 <= num, t <= 50`