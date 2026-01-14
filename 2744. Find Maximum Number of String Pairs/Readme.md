# 2744. Find Maximum Number of String Pairs

## Problem Description
You are given a **0-indexed** array `words` consisting of **distinct** strings.

The string `words[i]` can be paired with the string `words[j]` if:
* The string `words[i]` is equal to the reversed string of `words[j]`.
* `0 <= i < j < words.length`.

Return the **maximum** number of pairs that can be formed from the array `words`.

**Note:** Each string can belong in **at most one** pair.



## Examples

### Example 1:
**Input:** `words = ["cd","ac","dc","ca","zz"]`  
**Output:** `2`  
**Explanation:** In this example, we can form 2 pairs of strings:
- Pair `words[0]` ("cd") with `words[2]` ("dc").
- Pair `words[1]` ("ac") with `words[3]` ("ca").
It can be proven that 2 is the maximum number of pairs.

### Example 2:
**Input:** `words = ["ab","ba","cc"]`  
**Output:** `1`  
**Explanation:** Pair `words[0]` ("ab") with `words[1]` ("ba").

### Example 3:
**Input:** `words = ["aa","ab"]`  
**Output:** `0`  
**Explanation:** No pairs can be formed as "aa" is distinct and its reverse is itself, but it must be paired with a different index $j$.

## Constraints:
* `1 <= words.length <= 50`
* `words[i].length == 2`
* `words` consists of **distinct** strings.
* `words[i]` contains only lowercase English letters.