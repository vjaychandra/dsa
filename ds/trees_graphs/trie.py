class TrieNode:
    def __init__(self, val):
        self.val = val
        self.end = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        parent = self.root
        if not word:
            parent.end = True
        for char in word:
            node = TrieNode(char)
            if char not in parent.children:
                parent.children[char] = node
            parent = parent.children[char]
        parent.end = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end

    def startswith(self, prefix):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def lcp(self):
        # longest common prefix
        current = self.root
        if not current or current.end:
            return ""
        op = ""
        while current.children:
            for key in current.children:
                op += key
                current = current.children[key]
                if current.end:
                    return op
        return op            


if __name__ == "__main__":

    words = ["flower", "flower", "flower"]
    words = ["aa", "a"]

    trie = Trie()
    for word in words:
        trie.insert(word)
    #print(trie.startswith("fl"))
    print(trie.lcp())
