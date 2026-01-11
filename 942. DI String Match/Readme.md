# 942. DI String Match

## Problem Description
A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` can be represented as a string `s` of length `n` where:

* `s[i] == 'I'` if `perm[i] < perm[i + 1]`
* `s[i] == 'D'` if `perm[i] > perm[i + 1]`

Given a string `s`, reconstruct the permutation `perm` and return it. If there are multiple valid permutations, return **any of them**.



## Examples

### Example 1:
**Input:** `s = "IDID"`  
**Output:** `[0,4,1,3,2]`  
**Explanation:** - `0 < 4` (I)
- `4 > 1` (D)
- `1 < 3` (I)
- `3 > 2` (D)

### Example 2:
**Input:** `s = "III"`  
**Output:** `[0,1,2,3]`  
**Explanation:** - `0 < 1` (I)
- `1 < 2` (I)
- `2 < 3` (I)

### Example 3:
**Input:** `s = "DDI"`  
**Output:** `[3,2,0,1]`  
**Explanation:** - `3 > 2` (D)
- `2 > 0` (D)
- `0 < 1` (I)

## Constraints:
* `1 <= s.length <= 10^5`
* `s[i]` is either `'I'` or `'D'`.