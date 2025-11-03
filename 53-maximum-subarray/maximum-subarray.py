'''class Solution(object):
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float('-inf')  

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum'''

#Another code i found was better than mine
class Solution(object):
    def maxSubArray(self, nums):
        max_sum=nums[0]
        current_sum=0
        for i in nums:
            if current_sum <0:
                current_sum=0
            current_sum+=i
            if current_sum > max_sum:
                max_sum =current_sum
        return max_sum
