class Solution(object):
    def removeElement(self, nums, val):
        
        newNums=[]
      

        for i in nums:
            if val != nums[i]:
                newNums.append(nums[i])
            
        return len(newNums)

result = Solution()

nums = [3,2,2,3]
val = 3

print(result.removeElement(nums, val))