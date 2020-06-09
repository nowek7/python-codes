class Solution:
    def isUgly(self, aNumber: int) -> bool:
        if aNumber <= 0:
            return False
        else:
            if aNumber == 1:
                return True

            checkNumber = aNumber
            for prime in [2, 3, 5]:
                res = int(checkNumber % prime)
                while res == 0:
                    checkNumber = checkNumber / prime
                    res = int(checkNumber % prime)

            return checkNumber == 1


solution = Solution()
print(solution.isUgly(6))
print(solution.isUgly(8))
print(solution.isUgly(14))
print(solution.isUgly(-21))
print(solution.isUgly(0))
