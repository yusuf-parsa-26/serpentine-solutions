class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num = []

        for i in range(len(nums)):
            num.append((nums[i],i))
        
        num.sort()
        left,right = 0, len(nums)-1

        while left < right:
            Sum = num[left][0] + num[right][0]
            if Sum == target:
                return [num[left][1],num[right][1]]
            if Sum < target:
                left += 1
            else:
                right -= 1
        return [-1,-1]
