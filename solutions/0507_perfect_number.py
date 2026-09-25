class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        result = 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                result += i

                other_divisor = num // i

                if other_divisor != i:
                    result += other_divisor

        return result == num
