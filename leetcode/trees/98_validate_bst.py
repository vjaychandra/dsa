# validate bst

"""
idea is to check tree on bst principle

root.left < root < root.right

1. Inorder Traversal -> output list
    iterate list and check the bst principle
2. Using Recursion
    -> func => bst(root, left, right)
    -> base conditions:
        1. empty root -> True
        2. left_root and left_root_val >= root_val -> False
        3. right_root and right_root_val <= root_val -> False
        4. bst(left_root, root, entire_left) and bst(root.right, root, entire_right)


    def is_valid(self, root, left=None, right=None):
        
        if not root:
            return True
        
        if left and left.val >= root.val:
            return False
        
        if right and right.val <= root.val:
            return False
        
        return self.is_valid(root.left, left, root) and self.is_valid(root.right, root, right)
"""
