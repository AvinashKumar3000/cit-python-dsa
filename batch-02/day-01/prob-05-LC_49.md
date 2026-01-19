```python
class Solution:
    def sort(self, word):
        return "".join(sorted(word))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            sorted_word = self.sort(word)
            if sorted_word not in anagram:
                anagram[sorted_word] = []
            anagram[sorted_word].append(word)
        result = []
        for key in anagram:
            result.append(anagram[key])
        return result

```