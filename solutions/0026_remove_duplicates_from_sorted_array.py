class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = set(nums)
        arr = list(unique)
        arr.sort()

        for i in range(len(arr)):
            nums[i] = arr[i]
        
        return len(arr)
