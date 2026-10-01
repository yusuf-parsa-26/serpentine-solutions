class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] != 0:
            return 0

        num = nums[0] + 1
        for i in range(1,n):
            if nums[i] != num:
                return num
            else:
                num += 1
            
        return n
