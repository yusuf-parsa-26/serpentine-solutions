class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = 0
        max_sum = float("-inf")
        for i in range(len(nums)):
            sum += nums[i]
            max_sum = max(sum,max_sum)
            if sum < 0:
                sum = 0
        return max_sum
