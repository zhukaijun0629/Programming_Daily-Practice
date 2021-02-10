"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a list of words, for each word find the shortest unique prefix. You can
assume a word will not be a substring of another word (ie play and playing
won't be in the same words list)

Example
Input: ['joma', 'john', 'jack', 'techlead']
Output: ['jom', 'joh', 'ja', 't']
"""


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
        dic["*"] = True  # marks the end of the word

    def getPrefix(self, word):
        dic = self.dic
        prefix = ""
        for c in word:
            prefix += c
            if dic[c]["freq"] == 1:
                break
            else:
                dic = dic[c]
        return prefix


def shortest_unique_prefix(words):
    t = Trie()
    for word in words:
        t.addWord(word)
    res = []
    for word in words:
        prefix = t.getPrefix(word)
        res.append(prefix)
    return res


print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']
