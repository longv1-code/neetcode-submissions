class Node():
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.store = {}

    def insert(self, word: str) -> None:
        c = word[0]
        if c not in self.store:
            self.store[c] = Node()
        curr = self.store[c]
        for c in word[1:]:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = Node()
                curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        if word[0] not in self.store:
            return False
        curr = self.store[word[0]]
        for c in word[1:]:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.store:
            return False
        curr = self.store[prefix[0]]
        for c in prefix[1:]:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True