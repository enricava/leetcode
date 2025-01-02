from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']

        countUpToN = [0]
        acc = 0
        for i, w in enumerate(words):
            acc += 1 if w[0] in vowels and w[-1] in vowels else 0
            countUpToN.append(acc)

        return [countUpToN[q1+1] - countUpToN[q0] for q0, q1 in queries]
