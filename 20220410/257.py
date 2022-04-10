from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        print(self.dfs(root))

    def dfs(self, root):
        if root.left is None and root.right is None:
            return list(root.val)
        if root.left.val != 'null':
            l = self.dfs(root.left)
            if root.right.val != 'null':
                r = self.dfs(root.right)
            ans = list(l.append(root.val))
            ans.append(list(r.append(root.val)))
            return ans
        elif root.right.val != 'null':
            l = self.dfs(root.right)
            ans = list(l.append(root.val))
            return ans
        else:
            return list(root.val)


if __name__ == '__main__':
    A, B, C, D, E = [TreeNode(x) for x in [1, 2, 3, 'null', 5]]
    A.left, A.right = B, C
    B.left, B.right = D, E
    s = Solution()
    s.binaryTreePaths(A)
