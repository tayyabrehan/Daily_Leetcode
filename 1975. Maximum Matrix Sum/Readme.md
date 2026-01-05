# 1975. Maximum Matrix Sum

## Problem Description
You are given an `n x n` integer `matrix`. You can do the following operation **any number of times**:

* Choose any two **adjacent** elements of the `matrix` and **multiply** each of them by `-1`.

Two elements are considered adjacent if and only if they share a border.

Your goal is to **maximize** the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

## Examples

### Example 1:

**Input:** `matrix = [[1,-1],[-1,1]]`  
**Output:** `4`  
**Explanation:** We can reach a sum of 4 by:
1.  Multiplying the 2 elements in the first row by -1: `[[-1, 1], [-1, 1]]`
2.  Multiplying the 2 elements in the first column by -1: `[[1, 1], [1, 1]]`
The sum is now $1 + 1 + 1 + 1 = 4$.

### Example 2:
**Input:** `matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]`  
**Output:** `16`  
**Explanation:** We can follow the operation to flip signs until only one or zero negative signs remain. In this case, flipping the last two elements in the second row leads to a total sum of 16.

## Constraints:
* `n == matrix.length == matrix[i].length`
* `2 <= n <= 250`
* `-10^5 <= matrix[i][j] <= 10^5`

---

## 💡 Key Insight
1.  **Parity of Negatives:** Since we flip two adjacent numbers at a time, we can move a negative sign anywhere in the matrix. 
2.  If the total count of negative numbers is **even**, we can eventually make all numbers positive.
3.  If the total count is **odd**, one negative sign will always remain. To maximize the sum, we must ensure the negative sign is placed on the number with the **smallest absolute value**.