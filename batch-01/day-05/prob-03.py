# prob 03  word ladder
from collections import deque

class Solution:
    def ladderLength(self,beginWord,endWord,wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q = deque([ (beginWord, 1) ])

        while len(q) != 0:
            word, step = q.pop()
            if word == endWord:
                return step
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch +word[i+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        q.appendleft((new_word, step+1))

        return 0