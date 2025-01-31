

class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return 0
        

        for i in range (len(strs[0])):

            char = strs[0][i]


            for string in strs:
                if i>= len(string) or string[i] != char:
                     return strs[0][:i]
        
        return strs[0] 

result= Solution()
stri= ["flower","flow","flight"]
print(result.longestCommonPrefix(stri))
