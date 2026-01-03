# 1411. Number of Ways to Paint N × 3 Grid

## Problem Description
You have a grid of size `n x 3` and you want to paint each cell of the grid with exactly one of the three colors: **Red**, **Yellow**, or **Green**. 

You must ensure that **no two adjacent cells** have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given `n`, the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed **modulo 10^9 + 7**.



## Examples

### Example 1:
**Input:** `n = 1`  
**Output:** `12`  
**Explanation:** There are 12 possible ways to paint a 1x3 grid:
- 6 ways to use 3 colors (e.g., Red-Yellow-Green, Green-Yellow-Red, etc.)
- 6 ways to use 2 colors (e.g., Red-Yellow-Red, Yellow-Green-Yellow, etc.)

### Example 2:
**Input:** `n = 5000`  
**Output:** `30228214`  

## Constraints:
* `n == grid.length`
* `1 <= n <= 5000`

---

## Technical Note
This problem is typically solved using **Dynamic Programming**. The patterns in each row can be categorized into two types:
1.  **ABA Pattern** (Using 2 colors)
2.  **ABC Pattern** (Using 3 colors)

The number of ways to paint the next row depends on which pattern was used in the current row.