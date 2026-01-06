from collections import deque

# 1. TreeNode class define karni padti hai
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root) -> int:
        if not root:
            return 0
        
        max_sum = float('-inf') 
        ans_level = 1
        current_level = 1
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if current_level_sum > max_sum:
                max_sum = current_level_sum
                ans_level = current_level
            
            current_level += 1
            
        return ans_level

# 2. Tree banana (Example 1: [4,4,0,6,-8])
# Level 1
root = TreeNode(4)
# Level 2
root.left = TreeNode(4)
root.right = TreeNode(0)
# Level 3
root.left.left = TreeNode(6)
root.left.right = TreeNode(-8)

# 3. Solution run karna
sol = Solution()
print("Result Level:", sol.maxLevelSum(root))