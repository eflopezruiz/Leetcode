class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        reverse = 0
        if (x < 0):
            sign *= -1
        x = abs(x)
        while (abs(x) > 0):
            lastDigit = x % 10
            reverse = (reverse * 10) + lastDigit
            x = x // 10
        reverse = reverse*sign
        if (reverse <= -2**31) | (reverse >= (2**31 -1)):
            return 0
        return reverse