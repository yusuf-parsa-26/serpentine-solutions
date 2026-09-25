class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)  # Reverse the entire array
        reverse(0, k - 1)  # Fix the order of the first k elements
        reverse(k, n - 1)  # Fix the order of the remaining elements
