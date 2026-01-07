class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_sum = root.val 
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
        
