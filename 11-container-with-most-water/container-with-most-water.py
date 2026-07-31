class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height)-1
        max_area = 0

        while l<r:
            small = min(height[l],height[r])
            dis = abs(l-r)
            area = small * dis

            if area > max_area:
                max_area = area

            if small == height[l]:
                l = l + 1
            else:
                r = r - 1
            

        return max_area


            
             



        