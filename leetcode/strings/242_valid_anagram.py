# idea is to sort or store chars in dict and compare

def isAnagram(s, t):
    s1 = sum(ord(i) for i in s)
    s2 = sum(ord(i) for i in t)

    if s1 == s2 and set(s) == set(t):
        return True
    return False

s = "rat"
t = "car"
print(isAnagram(s, t))

