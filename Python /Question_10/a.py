class Solution(object):
    def strStr(self, haystack, needle):

        index=0 

        for i in haystack:
            if needle== haystack:
                index= i
            else: 
                index= -1
        return index       

result =Solution()

haystack = "sadbutsad"
needle = "sad"

print(result.strStr(haystack, needle))