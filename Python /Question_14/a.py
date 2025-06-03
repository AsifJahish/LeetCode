class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
 
    

        f=int(a, 2)+int (b, 2)
        return bin(f)[2:]




result = Solution()



a = "1010"
b = "1011"
print(result.addBinary(a, b), end= '')