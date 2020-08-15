# idea is to traverse string from first and last
# compare characters at index
# consider only alphanumeric chars

def isPalindrome(s):

    start = 0
    end = len(s) - 1

    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1
        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True

s = "race a car"
print(isPalindrome(s))
