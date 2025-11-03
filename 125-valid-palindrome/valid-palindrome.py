class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned=""
        c=0
        for i in s:
            if i.isalnum():
                cleaned+=i.lower()
        for i in range(len(cleaned)//2):
            if cleaned[i]==cleaned[-(i+1)]:
                c+=1
        if c==len(cleaned)//2:
            return True
        else:
            return False 
        
        