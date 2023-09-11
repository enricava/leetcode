// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        n = len(haystack) - 1
        m = len(needle) - 1
        while i < n:
            j = 0
            while haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m + 1:
                    return i - m - 1
                if i == n:
                    return -1
            i += 1
        return -1
            