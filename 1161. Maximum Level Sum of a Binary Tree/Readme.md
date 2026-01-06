# 1161. Maximum Level Sum of a Binary Tree

## Problem Description
Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the **smallest level x** such that the sum of all the values of nodes at level `x` is **maximal**.



## Examples

### Example 1:
**Input:** `root = [1,7,0,7,-8,null,null]`  
**Output:** `2`  
**Explanation:** - Level 1 sum = 1.
- Level 2 sum = 7 + 0 = 7.
- Level 3 sum = 7 + -8 = -1.
The maximum sum is 7, which occurs at **level 2**.

### Example 2:
**Input:** `root = [989,null,10250,98693,-89388,null,null,null,-32127]`  
**Output:** `2`

## Constraints:
* The number of nodes in the tree is in the range `[1, 10^4]`.
* `-10^5 <= Node.val <= 10^5`

---

## 🛠️ Approach
This problem is best solved using **Breadth-First Search (BFS)**, also known as **Level Order Traversal**. 

1. Use a **Queue** to traverse the tree level by level.
2. For each level, calculate the sum of all node values.
3. Keep track of the `maxSum` encountered so far and the corresponding `level`.
4. If a new `levelSum` is strictly greater than `maxSum`, update `maxSum` and the result level.