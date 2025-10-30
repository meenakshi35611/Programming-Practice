class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        a=0
        for i,num in enumerate(nums):
            a=target-num
            if a in seen:
                return [seen[a],i]
            seen[num]=i
        