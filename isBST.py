class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def inOrder(root, lst):
            if root == None: return
            inOrder(root.left, lst)
            lst.append(root.data)
            inOrder(root.right, lst) 
            
        lst = []
        if root == None:
            return True
        inOrder(root, lst)
        for i in range(1, len(lst)):
            if lst[i] <= lst[i - 1]:
                return False
        return True
        
