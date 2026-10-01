class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []
        index = 0
        def solve(index,subset):
            if index >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[index])
            solve(index+1,subset)
            subset.pop()
            solve(index+1,subset)
        solve(index,subset)
        return result
