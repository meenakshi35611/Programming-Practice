class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i]  not in s[:i]:
                if s.count(s[i])==1:
                    return i
        return -1
        