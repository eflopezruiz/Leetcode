class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        res = 0
        negative = 1
        MAX_INT = 2 ** 31 -1
        MIN_INT = -2 ** 31

        #Whitespace
        while i < len(s) and s[i] == ' ':
            i += 1

        #Symbols
        if i < len(s) and s[i] == '-':
            i += 1
            negative = -1
        elif i < len(s) and s[i] == '+':
            i += 1

        #Digits
        digits = set('0123456789')
        while i < len(s) and s[i] in digits:
            res = res *10 + int(s[i])
            i += 1

        #Last constraints
        res = res * negative
        if res < 0:
            return max(res,MIN_INT)
        return min(res,MAX_INT)