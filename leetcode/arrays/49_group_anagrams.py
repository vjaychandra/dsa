
def groupAnagrams(strs):

    gdct = {}

    for word in strs:
        w = tuple(sorted(word))
        gdct[w] = gdct.get(w, []) + [word]
    return [ gdct[key] for key in gdct ]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
