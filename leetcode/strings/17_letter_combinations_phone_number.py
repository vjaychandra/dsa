mapping = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
    }

def letterCombinations(digits):

    if not digits:
        return []

    if len(digits) == 1:
        return mapping[digits[0]]

    stack = []
    result = []
    chars = mapping[digits[0]]

    for digit in digits[1:]:
        stack.extend(mapping[digit])

    for char in chars:
        for item in stack:
            result.append(char+item)            
    return result    


print(letterCombinations("234"))

# output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
