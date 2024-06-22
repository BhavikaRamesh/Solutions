class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stack = []
        for i in x:
            if i in ["[", "(", "{"]:
                stack.append(i)
            else:
                if not stack:
                    return False
                popChar = stack.pop()
                if popChar == '{' and i != '}':
                    return False
                if popChar == '(' and i != ')':
                    return False
                if popChar == '[' and i != ']':
                    return False
        if stack:
            return False
        return True
