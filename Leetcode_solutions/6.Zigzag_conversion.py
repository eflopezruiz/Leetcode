class Solution:
    def convert(self, s: str, numRows: int) -> str:
        t = {}
        c = 0
        b = -1
        if numRows ==1:
            return s
        else:
            for i in range(len(s)):
                t[i] = c
                if c == (numRows-1):
                    b = b*-1
                if c == 0:
                    b = b*-1
                c = c+b

            sorted_t = sorted(t.items(),key=lambda x: x[1], reverse=False)

            a = ''
            for i in range(len(sorted_t)):
                    a = a + s[sorted_t[i][0]]
            return a