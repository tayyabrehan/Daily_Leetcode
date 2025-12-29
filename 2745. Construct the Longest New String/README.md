# 2745. Construct the Longest New String

## Problem Description
You are given three integers `x`, `y`, and `z`.

You have:
* `x` strings equal to `"AA"`
* `y` strings equal to `"BB"`
* `z` strings equal to `"AB"`

You want to choose some (possibly all or none) of these strings and concatenate them in some order to form a new string. This new string must not contain `"AAA"` or `"BBB"` as a substring.

Return the **maximum possible length** of the new string.

A **substring** is a contiguous non-empty sequence of characters within a string.

## Examples

### Example 1:
**Input:** `x = 2, y = 5, z = 1`  
**Output:** `12`  
**Explanation:** We can concatenate the strings `"BB"`, `"AA"`, `"BB"`, `"AA"`, `"BB"`, and `"AB"` in that order. The new string is `"BBAABBAABBAB"`.  
This string has length 12, and it is the maximum possible.

### Example 2:
**Input:** `x = 3, y = 2, z = 2`  
**Output:** `14`  
**Explanation:** We can concatenate the strings `"AB"`, `"AB"`, `"AA"`, `"BB"`, `"AA"`, `"BB"`, and `"AA"` in that order. The new string is `"ABABAABBAABBAA"`.  
This string has length 14, and it is the maximum possible.

## Constraints:
* `1 <= x, y, z <= 50`