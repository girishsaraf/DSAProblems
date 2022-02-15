class Solution(object):
    def isValid(self, s):
        new_stack = [s[0]]
        for i in range(1, len(s)):
            if len(new_stack) > 0 and ((new_stack[-1] == '(' and s[i] == ')') or (new_stack[-1] == '[' and s[i] == ']') or (new_stack[-1] == '{' and s[i] == '}')):
                new_stack = new_stack[:-1]
            else:
                new_stack.append(s[i])
        if len(new_stack) == 0:
            return True
        return False
            
        
                
        