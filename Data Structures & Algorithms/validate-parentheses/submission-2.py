class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif len(stack) > 0:
                if c == ')':
                    if stack[-1] != '(':
                        return False
                    stack.pop(-1)
                elif c == '}':
                    if stack[-1] != '{':
                        return False
                    stack.pop(-1)
                else:
                    if stack[-1] != '[':
                        return False
                    stack.pop(-1)
            else:
                return False
        if len(stack) == 0:
            return True
        return False