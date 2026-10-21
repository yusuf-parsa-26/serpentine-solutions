class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result.append(mid)

                for i in range(mid + 1, right + 1): 
                    if nums[i] == target:
                        result.append(i)

                right = mid - 1  

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return sorted(result) 
