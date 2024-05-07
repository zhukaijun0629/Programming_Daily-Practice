"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given a list of words in a string, reverse the words in-place (ie don't create a new string and reverse the words). Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).
"""


def reverse_words(words):
    # Fill this in.
    if not words:
        return 
    words.reverse()
    word_start_idx = 0
    for idx, c in enumerate(words):
        if c == " " and words[idx - 1]:
            reverse_cur_word(words, word_start_idx, idx - 1)
            word_start_idx = idx + 1
    reverse_cur_word(words,word_start_idx, len(words) - 1)
    return


def reverse_cur_word(words, start_idx, end_idx):
    while start_idx < end_idx:
        words[start_idx], words[end_idx] = words[end_idx], words[start_idx]
        start_idx += 1
        end_idx -= 1
    return



s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can
