class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        length= 0
        s= s.rstrip()
        
        for i in reversed((s)):
            if i==" ":
                break
            length+=1
        return length
           
                

s = "luffy is still joyboy"

result= Solution()

print(result.lengthOfLastWord(s))