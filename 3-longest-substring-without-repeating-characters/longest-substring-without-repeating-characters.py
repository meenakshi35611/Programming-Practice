class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=dict()
        left=max_len=0

        for r in range(len(s)):
            if s[r] in d and d[s[r]]>=left:
                left=d[s[r]]+1
            d[s[r]]=r
            max_len=max(max_len,r-left+1)
        return max_len
                
            



            

            

        