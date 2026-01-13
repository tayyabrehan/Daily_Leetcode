# 3453. Separate Squares I

## Problem Description
You are given a 2D integer array `squares`. Each `squares[i] = [xi, yi, li]` represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the **minimum** y-coordinate value of a horizontal line such that the total area of the squares above the line **equals** the total area of the squares below the line.

**Note:** * Squares may overlap. Overlapping areas should be counted multiple times.
* Answers within $10^{-5}$ of the actual answer will be accepted.



## Examples

### Example 1:
**Input:** `squares = [[0,0,1],[2,2,1]]`  
**Output:** `1.00000`  
**Explanation:** - Total area = $1 \times 1 + 1 \times 1 = 2$. 
- We need 1 unit of area below the line and 1 unit above. 
- Any horizontal line between $y = 1$ and $y = 2$ satisfies this. The lowest value is $1$.

### Example 2:
**Input:** `squares = [[0,0,2],[1,1,1]]`  
**Output:** `1.16667`  
**Explanation:** - Total area is $2^2 + 1^2 = 5$. Target area for each side is $2.5$.
- Below the line ($y = 7/6$): Area is $2 \times (7/6) + 1 \times (1/6) = 14/6 + 1/6 = 15/6 = 2.5$.
- Above the line: Area is $15/6 = 2.5$.
- The output is $7/6 \approx 1.16667$.

## Constraints:
* `1 <= squares.length <= 5 * 10^4`
* `squares[i] = [xi, yi, li]`
* `0 <= xi, yi <= 10^9`
* `1 <= li <= 10^9`
* The total area of all the squares will not exceed $10^{12}$.