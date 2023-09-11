// https://leetcode.com/problems/length-of-last-word

class Solution(object):
    import re
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(re.split('[ ]+', s.rstrip())[-1])