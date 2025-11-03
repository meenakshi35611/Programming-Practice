class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=set()
        for i in range(len(s)):
                if s[i] not in a and s.count(s[i])==1:
                    return i
                a.add(s[i])
        return -1
        