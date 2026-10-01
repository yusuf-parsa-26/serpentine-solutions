class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []
        subset = []

        def solve(index):
            if index >= len(nums):
                result.append(subset.copy())
                return

            # Include nums[index]
            subset.append(nums[index])
            solve(index + 1)

            # Backtrack
            subset.pop()

            # Skip duplicate values
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            # Exclude nums[index]
            solve(index + 1)

        solve(0)

        return result
        
