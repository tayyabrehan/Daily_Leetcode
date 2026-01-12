# 1266. Minimum Time Visiting All Points

## Problem Description
On a 2D plane, there are `n` points with integer coordinates `points[i] = [xi, yi]`. Return the **minimum time** in seconds to visit all the points in the order given by `points`.

You can move according to these rules:
* In **1 second**, you can either:
    * Move vertically by one unit,
    * Move horizontally by one unit, or
    * Move diagonally $\sqrt{2}$ units (moving one unit vertically and one unit horizontally simultaneously).
* You must visit the points in the **same order** as they appear in the array.
* You are allowed to pass through points that appear later in the order, but these do not count as visits.



## Examples

### Example 1:
**Input:** `points = [[1,1],[3,4],[-1,0]]`  
**Output:** `7`  
**Explanation:** One optimal path is:
1. `[1,1] -> [3,4]` : 3 seconds (Moving 2 units diagonally and 1 unit vertically)
2. `[3,4] -> [-1,0]` : 4 seconds (Moving 4 units diagonally)
**Total time = 7 seconds**

### Example 2:
**Input:** `points = [[3,2],[-2,2]]`  
**Output:** `5`  
**Explanation:** Moving horizontally from $x=3$ to $x=-2$ takes 5 seconds.

## Constraints:
* `n == points.length`
* `1 <= n <= 100`
* `points[i].length == 2`
* `-1000 <= points[i][0], points[i][1] <= 1000`