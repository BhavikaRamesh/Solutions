//1st approach doing by following in-order traversal
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
// 2nd Approach doing recursively     
class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def helper(root, mini, maxi):
            if root == None: return True
            elif mini < root.data and maxi > root.data:
                return helper(root.left, mini, root.data) and helper(root.right, root.data, maxi)
            return False
            
        lst = []
        if root == None:
            return True
        elif helper(root.left, 0, root.data) and helper(root.right, root.data, 1000000):
            return True
        return False
