class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left, right = 0, 0
        max_count = 0
        count = 0

        while right < len(nums):
            if nums[right] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
                left = right + 1

            right += 1

        return max_count
