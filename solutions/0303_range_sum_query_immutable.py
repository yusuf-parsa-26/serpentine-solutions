class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]

        return self.prefix_sum[right] - self.prefix_sum[left - 1]
