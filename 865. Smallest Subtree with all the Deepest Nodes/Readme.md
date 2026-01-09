# 865. Smallest Subtree with all the Deepest Nodes

## Problem Description
Given the `root` of a binary tree, the depth of each node is the shortest distance to the root.

Return the **smallest subtree** such that it contains **all the deepest nodes** in the original tree.

* A node is called **the deepest** if it has the largest depth possible among any node in the entire tree.
* The **subtree** of a node is a tree consisting of that node, plus the set of all descendants of that node.



## Examples

### Example 1:
**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4]`  
**Output:** `[2,7,4]`  
**Explanation:** - The deepest nodes are `7` and `4` (depth 3).
- The smallest subtree containing both is the subtree starting at node `2`.
- Note: Nodes `5` and `3` also contain these deepest nodes, but the subtree at node `2` is the smallest.

### Example 2:
**Input:** `root = [1]`  
**Output:** `[1]`  
**Explanation:** The root is the deepest node in the tree.

### Example 3:
**Input:** `root = [0,1,3,null,2]`  
**Output:** `[2]`  
**Explanation:** The deepest node is `2`. The smallest subtree containing it is the node `2` itself.

## Constraints:
* The number of nodes in the tree will be in the range `[1, 500]`.
* `0 <= Node.val <= 500`
* The values of the nodes in the tree are **unique**.

---
**Note:** This question is the same as LeetCode 1123: [Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/).