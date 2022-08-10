class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        rev = 0
        while y > 0: 
            rev = rev * 10 + (y % 10)
            y = y // 10
        if rev == x:
            return True
        else:
            return False