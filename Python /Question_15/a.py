import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """ 
        if x == 0 or x == 1:
            return x  # Handle edge cases
        
        left, right = 1, x
        ans = 0  # Store result
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid  # Perfect square case
            elif mid * mid < x:
                ans = mid  # Store the largest possible integer sqrt
                left = mid + 1
            else:
                right = mid - 1

        return ans 

result =Solution()

a=8

print(result.mySqrt(a))