# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        queue = [root]
        
        while queue:
            tem = queue.pop()
            if tem.left!= None:
                queue.append(tem.left)
            if tem.right!= None:
                queue.append(tem.right)
                
            if tem.left!= None or tem.right!=None:
                tem2 = tem.left
                tem.left = tem.right
                tem.right = tem2
        
        return root
           
