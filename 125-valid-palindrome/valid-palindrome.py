import re
class Solution(object):
    def isPalindrome(self, s):
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if cleaned[::-1]==cleaned:
            return True 
        return False
        