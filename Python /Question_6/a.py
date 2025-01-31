class Solution(object):
    def isValid(self, s):
        stuck=[]

        valid = {')': '(', '}': '{', ']': '['} 

        for char in s:
            if char in valid:
                if stuck and stuck[-1]== valid[char]:
                    stuck.pop()
                else:
                    return False
            else:
                stuck.append(char)

        return not stuck


result = Solution()

str= "()"

print(result.isValid(str))