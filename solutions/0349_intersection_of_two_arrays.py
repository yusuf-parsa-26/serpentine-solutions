class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen1 = set()
        seen2 = set()

        for i in range(len(nums1)):
            seen1.add(nums1[i])

        for i in range(len(nums2)):
            seen2.add(nums2[i])
        
        nums = list(seen2)
        List = []
        for i in range(len(nums)):
            if nums[i] in seen1:
                List.append(nums[i])
        return List
