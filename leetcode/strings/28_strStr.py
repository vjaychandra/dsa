# idea is to search the substring in the main string
# at every iteration from i to i+len(substring)
# range -> main_string-substring, see pt2

def strStr(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(strStr("hello", "ll"))
