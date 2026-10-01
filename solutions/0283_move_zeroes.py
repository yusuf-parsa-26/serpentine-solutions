class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums) == 0:
            return nums
        
        arr = []
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                arr.append(nums[i])
                k += 1
        
        for i in range(k):
            nums[i] = arr[i]
        
        for i in range(k, len(nums)):
            nums[i] = 0
