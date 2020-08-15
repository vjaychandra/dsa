
def firstUniqChar(s):

    sdict = {}

    for index, char in enumerate(s):
        if not sdict.get(char):
            sdict[char] = 1
        else:
            sdict[char] += 1
    
    for char in sdict:
        if sdict[char] == 1:
            return s.index(char)

    return -1

s = "loveleetcode"
print(firstUniqChar(s))
