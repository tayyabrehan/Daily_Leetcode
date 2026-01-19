# 222. Count Complete Tree Nodes

## Problem Description
Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.

According to **Wikipedia**, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and $2^h$ nodes inclusive at the last level $h$.

Design an algorithm that runs in less than $O(n)$ time complexity.



## Examples

### Example 1:
**Input:** `root = [1,2,3,4,5,6]`  
**Output:** `6`  
**Explanation:** The tree has 3 levels. Levels 1 and 2 are fully filled, and level 3 has 3 nodes. Total = 6.

### Example 2:
**Input:** `root = []`  
**Output:** `0`

### Example 3:
**Input:** `root = [1]`  
**Output:** `1`

## Constraints:
* The number of nodes in the tree is in the range `[0, 5 * 10^4]`.
* `0 <= Node.val <= 5 * 10^4`
* The tree is guaranteed to be **complete**.

---

## 💡 Efficiency Note
While a simple DFS/BFS traversal would take $O(n)$ time, a more efficient approach utilizes the properties of a complete binary tree. By comparing the left and right heights of the tree, you can determine if a subtree is "perfectly" filled, allowing you to use the formula $2^{height} - 1$ to skip counts for entire subtrees.