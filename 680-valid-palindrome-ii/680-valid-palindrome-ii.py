class Solution(object):
    
    def checkPal(self, s):
        return s == s[::-1]
    
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            top, bottom = 0, len(s) - 1
            while(top < bottom):
                if s[top] != s[bottom]:
                    right, left = s[top:bottom], s[top + 1:bottom + 1]
                    return right == right[::-1] or left == left[::-1]
                top, bottom = top + 1, bottom - 1
            return True
            
                
        