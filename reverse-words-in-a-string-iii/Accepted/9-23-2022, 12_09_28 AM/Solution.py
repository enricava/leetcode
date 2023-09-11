// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(w):
            ret = ''
            for i in range(1,len(w)+1):
                ret+=w[-i]
            return ret
        d = s.split(' ')
        return ' '.join([reverse(w) for w in d])