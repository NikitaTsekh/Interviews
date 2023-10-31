#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



def check_maxDepth():
    """
    unit test for Solution class method maxDepth

    """
    obj_=Solution()
    assert obj_.maxDepth(root = [3,9,20,null,null,15,7]) ==3
    assert obj_.maxDepth(root = [1,null,2]) == 2

check_maxDepth()