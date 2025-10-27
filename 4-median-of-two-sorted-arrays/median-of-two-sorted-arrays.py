class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged=sorted(nums1+nums2)
        length=len(merged)
        i=length//2
        med=0
        if length%2==0:
            med=float(merged[i-1]+merged[i])/2
        else:
            med=float(merged[i])
        return med
            
        