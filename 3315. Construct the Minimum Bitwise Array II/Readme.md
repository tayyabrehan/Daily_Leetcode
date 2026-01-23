# 3315. Construct the Minimum Bitwise Array II

## Problem Description
You are given an array `nums` consisting of `n` **prime** integers.

You need to construct an array `ans` of length `n`, such that, for each index `i`, the bitwise **OR** of `ans[i]` and `ans[i] + 1` is equal to `nums[i]`:

$$ans[i] \text{ OR } (ans[i] + 1) == nums[i]$$

Additionally, you must **minimize** each value of `ans[i]` in the resulting array. If it is **not possible** to find such a value for `ans[i]` that satisfies the condition, then set `ans[i] = -1`.



## Examples

### Example 1:
**Input:** `nums = [2,3,5,7]`  
**Output:** `[-1,1,4,3]`  
**Explanation:** - For `i = 0`: No value satisfies `ans[0] OR (ans[0] + 1) = 2`, so `ans[0] = -1`.
- For `i = 1`: The smallest `ans[1]` is `1`, because `1 OR (1 + 1) = 3`.
- For `i = 2`: The smallest `ans[2]` is `4`, because `4 OR (4 + 1) = 5`.
- For `i = 3`: The smallest `ans[3]` is `3`, because `3 OR (3 + 1) = 7`.

### Example 2:
**Input:** `nums = [11,13,31]`  
**Output:** `[9,12,15]`  
**Explanation:** - For `i = 0`: The smallest `ans[0]` is `9`, because `9 OR 10 = 11`.
- For `i = 1`: The smallest `ans[1]` is `12`, because `12 OR 13 = 13`.
- For `i = 2`: The smallest `ans[2]` is `15`, because `15 OR 16 = 31`.

## Constraints:
* `1 <= nums.length <= 100`
* `2 <= nums[i] <= 10^9`
* `nums[i]` is a **prime number**.

---

### 💡 Hint for Large Constraints
For this version (II), the values of `nums[i]` can be up to $10^9$, so a linear search for `ans[i]` is not feasible. Consider the bitwise property: `x OR (x + 1)` only changes the first `0` bit from the right to a `1`. To minimize `ans[i]`, look for the lowest block of consecutive `1`s in the binary representation of `nums[i]` and flip the rightmost `1` in that block to `0`.