class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = None

    def insert(self, word):

        for char in word:
            node = TrieNode(
            
