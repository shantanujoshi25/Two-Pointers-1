# // Time Complexity : O(n^2)
# // Space Complexity : O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:  
                continue
                
            x, y = i + 1, len(nums) - 1
            
            while x < y:
                total = nums[i] + nums[x] + nums[y]
                
                if total == 0:
                    result.append([nums[i], nums[x], nums[y]])
                    
                    while x < y and nums[x] == nums[x + 1]:
                        x += 1
                    while x < y and nums[y] == nums[y - 1]:
                        y -= 1
                    x += 1
                    y -= 1
                elif total < 0: 
                    x += 1
                else:  
                    y -= 1
                    
        return result