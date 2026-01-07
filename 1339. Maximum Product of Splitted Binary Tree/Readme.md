# 1339. Maximum Product of Splitted Binary Tree

## Problem Description
Given the `root` of a binary tree, split the binary tree into two subtrees by removing **one edge** such that the product of the sums of the subtrees is maximized.

Return the **maximum product** of the sums of the two subtrees. Since the answer may be too large, return it **modulo 10^9 + 7**.

**Note:** You must maximize the answer *before* taking the modulo.



## Examples

### Example 1:
**Input:** `root = [1,2,3,4,5,6]`  
**Output:** `110`  
**Explanation:** Remove the edge between node 1 and node 3.
- Subtree 1 (Nodes 3, 6): Sum = $3 + 6 = 9$ (Wait, looking at standard split: $1+2+3+4+5+6 = 21$).
- If we split such that one sum is `11` and the other is `10`, the product is $11 \times 10 = 110$.

### Example 2:
**Input:** `root = [1,null,2,3,4,null,null,5,6]`  
**Output:** `90`  
**Explanation:** Remove the edge to get subtrees with sums `15` and `6`. Their product is $15 \times 6 = 90$.

## Constraints:
* The number of nodes in the tree is in the range `[2, 5 * 10^4]`.
* `1 <= Node.val <= 10^4`

---

## 💡 Strategy
1.  **Find Total Sum:** Traverse the entire tree once to calculate the total sum of all node values.
2.  **Calculate Subtree Sums:** Use a Post-order traversal (DFS) to calculate the sum of every possible subtree.
3.  **Maximize Product:** For each subtree sum `S`, the other part of the tree will have a sum of `TotalSum - S`. The product is `S * (TotalSum - S)`. Keep track of the maximum product found.
4.  **Modulo:** Apply the modulo $10^9 + 7$ only at the very end.