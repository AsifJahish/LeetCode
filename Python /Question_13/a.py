class Solution(object):
    def plusOne(self, digits):

        for i in reversed(range(len(digits))):

            if digits[i]< 9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
                return [1]+digits
        return [1]+digits

result= Solution()

digits = [1,2,3]

print(result.plusOne(digits))