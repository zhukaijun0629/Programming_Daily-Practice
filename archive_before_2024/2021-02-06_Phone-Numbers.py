"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a phone number, return all valid words that can be created using that phone number.

For instance, given the phone number 364
we can construct the words ['dog', 'fog'].
"""

import collections

lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

class Trie:
    def __init__(self):
        self.dic = {}
    
    def addWord(self, word):
        dic = self.dic
        for c in word:
            if c not in dic:
                dic[c] = {}
            dic = dic[c]
        dic['#'] = True
    
    def makeWords(self, phone):
        if not phone:
            return []
        dic = self.dic
        words = [('', dic)]
        for num in phone:
            if not words:
                break
            next_words = []
            for cur_word, cur_dic in words:
                for letter in lettersMaps[int(num)]:
                    if letter in cur_dic:
                        next_words.append((cur_word + letter, cur_dic[letter]))
            words = next_words
        
        res = []
        for cur_word, cur_dic in words:
            if cur_dic['#'] == True:
                res.append(cur_word)
        return res


def makeWords1(phone):
    # Fill this in
    letter2num = {}
    nums2words = collections.defaultdict(list)
    for num, letters in lettersMaps.items():
        for letter in letters:
            letter2num[letter] = str(num)
    for word in validWords:
        nums_list = [letter2num[letter] for letter in word]
        nums = ''.join(nums_list)
        nums2words[nums].append(word)
    return nums2words[phone]

def makeWords2(phone):
    t = Trie()
    for word in validWords:
        t.addWord(word)
    return t.makeWords(phone)



# print(makeWords1('364'))
# ['dog', 'fog']

print(makeWords2('364'))
# ['dog', 'fog']