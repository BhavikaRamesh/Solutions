class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        tokens = A
        stack = []
        for i in tokens:
            if i not in ['+', '*', '-', '/']:
                stack.append(int(i))
            else:
                right = stack.pop()
                left = stack.pop()
                if i == '+':
                    stack.append(left + right)
                elif i == '-':
                    stack.append(left - right)
                elif i == '/':
                    stack.append(int(left / right))
                else:
                    stack.append(left * right)
        return stack.pop()
