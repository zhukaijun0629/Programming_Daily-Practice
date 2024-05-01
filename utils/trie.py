class Trie:
    def __init__(self):
        self.dic = {}

    def addWord(self, word):
        dic = self.dic
        for c in word:
            if c not in dic:
                dic[c] = {"freq": 1}
            else:
                dic[c]["freq"] += 1
            dic = dic[c]
        dic["*"] = True # marks the end of words

    def generateUniquePrefix(self, word):
        dic = self.dic
        prefix = ""
        for c in word:
            prefix += c
            if dic[c]["freq"] == 1:
                break
            dic = dic[c]
        
        return prefix

def shortest_unique_prefix(words):
    t = Trie()
    for word in words:
        t.addWord(word)
    ans = []
    for word in words:
        prefix = t.generateUniquePrefix(word)
        ans.append(prefix)
    return ans

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']