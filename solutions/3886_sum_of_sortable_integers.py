from math import isqrt

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        
        pref_max = [0] * (n + 1)

        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        
        suff_min = [10**9] * (n + 1)

        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        
        pref_drop = [0] * n

        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1]

            if nums[i - 1] > nums[i]:
                pref_drop[i] += 1

        
        def can_sort(k):
            for start in range(0, n, k):
                end = start + k - 1

    
                if pref_max[start] > suff_min[start]:
                    return False
                    
                drops = pref_drop[end] - pref_drop[start]

                if nums[end] > nums[start]:
                    drops += 1

                if drops > 1:
                    return False

            return True

        
        answer = 0

        for d in range(1, isqrt(n) + 1):
            if n % d == 0:
                if can_sort(d):
                    answer += d

                other = n // d

                if other != d and can_sort(other):
                    answer += other

        return answer
