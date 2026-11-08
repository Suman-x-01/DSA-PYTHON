class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s=set(nums)
        arr=sorted(s)

        if len(s)>=3:
            return arr[-3]
        else:
            return arr[-1]