// https://leetcode.com/problems/number-of-matching-subsequences

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        i = 0
        ok = [True for _ in words]
        iterators = [0 for _ in words]
        count = 0
        while i < len(s) and any(ok):
            for k in range(len(words)):
                if ok[k] and words[k][iterators[k]] == s[i]:
                    iterators[k] += 1
                    if iterators[k] >= len(words[k]):
                        ok[k] = False
                        count += 1
            i += 1
        return count