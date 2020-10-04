# https://leetcode.com/problems/palindrome-number/

def is_palindrome(x):
    if x < 0:
        return False
    
    xstr = str(x)
    left, right = 0, len(xstr)
    
    while left < right:
        if xstr[left] != xstr[right]:
            return False
        left += 1
        right -= 1
    
    return True