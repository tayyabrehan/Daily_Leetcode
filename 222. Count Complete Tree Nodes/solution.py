from collections import deque
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        q=deque([(root)])
        r=0
        while q:
            l=len(q)
            r+=l
            for _ in range(l):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return r