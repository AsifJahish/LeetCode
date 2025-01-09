

def all_substring(s):
    substring=[]
    n= len(s)

    for i in range(n):
        for j in range(i+1, n+1):
            substring.append(s[i:j])
    return substring



string = "011101"

print(all_substring(string))