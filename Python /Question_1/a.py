# first of all we gonna try to write a code to divide to all possible sub string


def allSubstring(s):
    subtring = []
    n= len(s)
    for i in range(n):
        for j in range ( i+1, n+1):
            subtring.append(s[i:j]) 
            # we use the slice operation for this tto just slice it like from i 10 j 
    return subtring



string ="abc"
result = allSubstring(string)
print(result)