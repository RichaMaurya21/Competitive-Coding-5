# Find Largest Value in Each Tree Row 
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            size = len(q)
            maxRes = float(-inf)
            for i in range(size):
                current = q.popleft()
                if current.left:
                    q.append(current.left)

                if current.right:
                    q.append(current.right)

                maxRes = max(maxRes,current.val)

            res.append(maxRes)

        return res