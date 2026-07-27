class Solution:
    def myAtoi(self, s: str) -> int:

        num = 0
        digit_read = False
        sign_seen = False
        is_negative = False

        INT_MIN = -2147483648
        INT_MAX = 2147483647

        for char in s:

            if char == " ":

                if digit_read or sign_seen:
                    break
                
                continue
            
            elif char == "-" or char == "+":

                if digit_read or sign_seen:
                    break
                sign_seen = True

                if char == "-":
                    is_negative = True
            
            elif char.isdigit():
                digit_read = True
                num = (num*10) + int(char)

            else:
                break
        
        if is_negative:
            num = -num

        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num


        