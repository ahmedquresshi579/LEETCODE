class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_lenght = 0

        for i in range(len(s)):
            letters = []
            for j in range(i,len(s)):
                if s[j] in letters:
                    break
                else:
                    letters.append(s[j])

            if len(letters) > max_lenght:
                max_lenght = len(letters)

        return max_lenght
