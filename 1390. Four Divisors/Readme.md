# 1390. Four Divisors

## Problem Description
Given an integer array `nums`, return the sum of divisors of the integers in that array that have **exactly four divisors**. If there is no such integer in the array, return `0`.

A divisor of an integer `n` is an integer that divides `n` without leaving a remainder.

## Examples

### Example 1:
**Input:** `nums = [21,4,7]`  
**Output:** `32`  
**Explanation:** - **21** has 4 divisors: 1, 3, 7, 21. Sum = $1 + 3 + 7 + 21 = 32$.
- **4** has 3 divisors: 1, 2, 4.
- **7** has 2 divisors: 1, 7.
The answer is the sum of divisors of 21 only.

### Example 2:
**Input:** `nums = [21,21]`  
**Output:** `64`  
**Explanation:** Both numbers are 21, and each contributes 32 to the final sum.

### Example 3:
**Input:** `nums = [1,2,3,4,5]`  
**Output:** `0`  
**Explanation:** None of the numbers in the array have exactly four divisors.

## Constraints:
* `1 <= nums.length <= 10^4`
* `1 <= nums[i] <= 10^5`

---

## Logic Hint
An integer $n$ has exactly four divisors in two cases:
1.  It is the product of two distinct prime numbers ($n = p \times q$).
2.  It is the cube of a prime number ($n = p^3$).