class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = self.power(x, abs(n))
        return 1 / result if n < 0 else result

    def power(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        half = self.power(x, n // 2)

        if n % 2 == 0:
            return half * half

        return half * half * x
