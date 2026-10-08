class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word):
        n = self.root
        for char in word:
            if char not in n.children:
                n.children[char] = TrieNode()
            n = n.children[char]
        n.eow = True

    def search(self, word):
        n = self.root
        for char in word:
            if char not in n.children:
                return False
            n = n.children[char]
        return n.eow

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Construct Trie
        trie = Trie()
        max_len = 0
        for word in wordDict:
            trie.put(word)
            max_len = max(max_len, len(word))

        # DP (whether we could cleanly break s[i:])
        memo = [False] * (len(s) + 1)
        memo[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(i, min(len(s), i+max_len)):
                if trie.search(s[i:j+1]):
                    memo[i] = memo[j+1]

                if memo[i]:
                    break

        return memo[0]
        