# // Time Complexity : O(n)
# // Space Complexity : O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None: 
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # red = 0
        # blue = 0
        # white = 0

        # for i in nums:
        #     if(i == 0):
        #         red+=1
        #     elif(i == 1):
        #         blue+=1
        #     elif(i==2):
        #         white+=1
      
        
        # nums[:] = [0]*red + [1]*blue + [2]*white


        p0 = 0
        curr =0
        p2 = len(nums)-1

        while(curr<=p2):
            if(nums[curr] == 2):
                nums[p2],nums[curr] = nums[curr],nums[p2]
                p2-=1
            elif(nums[curr] == 0):
                nums[p0],nums[curr] = nums[curr],nums[p0]
                p0+=1
                curr+=1
            else:
                curr+=1