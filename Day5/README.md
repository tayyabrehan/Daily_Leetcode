# 2799. Count Complete Subarrays in an Array

## 📝 Problem Statement

You are given an array `nums` consisting of positive integers.

We call a subarray **complete** if the **number of distinct elements** in the subarray is equal to the **number of distinct elements in the entire array**.

Return the **number of complete subarrays**.

> A subarray is a contiguous, non-empty part of an array.

---

## ⌨️ Input

- An integer array `nums` of length `n`.

## 📤 Output

- An integer representing the number of **complete subarrays**.

---

## 🔒 Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2000`

---

## 🧪 Examples

Example 1  
Input: nums = [1, 3, 1, 2, 2]  
Output: 4  
Explanation:  
The total number of distinct elements in the full array is 3: {1, 2, 3}  
The complete subarrays are:  
- [1, 3, 1, 2]  
- [1, 3, 1, 2, 2]  
- [3, 1, 2]  
- [3, 1, 2, 2]

---

Example 2  
Input: nums = [5, 5, 5, 5]  
Output: 10  
Explanation:  
All elements are the same (only 1 distinct element), so every subarray is complete.  
Total subarrays = n * (n + 1) / 2 = 4 * 5 / 2 = 10

---

## 💡 Approach

1. Count how many unique elements exist in the whole array.
2. For each subarray, count the distinct elements.
3. If the distinct count of the subarray equals that of the full array, it's complete.
4. Brute-force works here due to small `n` (≤ 1000).

---
