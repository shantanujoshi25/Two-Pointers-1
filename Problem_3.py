# // Time Complexity : O(n)
# // Space Complexity : O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        l,r = 0,len(height) - 1
        while(l<r):
            tempWater = min(height[l],height[r]) * (r-l)
            if tempWater > maxWater : maxWater = tempWater
            if height[l]>height[r] : r=r-1
            else: l=l+1
        return maxWater