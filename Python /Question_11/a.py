    # 35. Search Insert Position

    class Solution(object):
        def searchInsert(self, nums, target):

            

            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                else:
                    nums.append(target)
                    nums.sort()

                    for j in range(len(nums)):
                        if nums[j]== target:
                            return j
            
    # nums = [1,3,5,6]
    # target = 5


    nums = [1,3,5,6]
    target = 7
    result = Solution()

    print(result.searchInsert(nums, target))