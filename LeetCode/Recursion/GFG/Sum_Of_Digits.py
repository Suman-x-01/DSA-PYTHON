class Solution:
    def sumOfDigits(self, n):
        if n<=0:
            return n
        return (n%10 )+ self.sumOfDigits(n//10)

s=Solution()
print(s.sumOfDigits(687))