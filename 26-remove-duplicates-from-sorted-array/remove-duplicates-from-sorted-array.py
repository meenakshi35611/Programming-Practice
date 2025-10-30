class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        unique=list(set(nums))
        unique.sort()
        l_u=len(unique)
        for i in range(l_u):
            nums[i]=unique[i]
        print("nums = ",nums[:l_u])
        return l_u