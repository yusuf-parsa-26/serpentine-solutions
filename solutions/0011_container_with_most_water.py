class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0
        left,right =0,len(height)-1

        while left < right:
            amount = min(height[left],height[right])*(right-left)
            maximum = max(maximum,amount)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
            
        return maximum
        
