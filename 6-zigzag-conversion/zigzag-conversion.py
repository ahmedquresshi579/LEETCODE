class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        matrix = [[] for _ in range(numRows)]

        direction = 1
        idx = 0

        for char in s:
            matrix[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows-1:
                d = -1
            
            idx = idx + d

        final_string = ""


        for row in matrix:
            final_string += "".join(row)


        return final_string
        