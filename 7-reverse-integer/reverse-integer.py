class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            sign = True
            x = -x
        else:
            sign = False

        temp = x
        digit_count = 0

        while temp > 0:
            digit_count = digit_count + 1
            temp = temp // 10

        temp = digit_count
        rev = 0

        while x>0:
            rem = x % 10
            x = x // 10
            digit_count = digit_count - 1 
            rev = rem * (10**digit_count) + rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        if sign:
            return -rev
        else:
            return rev



        