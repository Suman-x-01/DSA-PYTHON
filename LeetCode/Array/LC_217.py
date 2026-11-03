class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for n in nums:
            s.add(n)
        return len(s) != len(nums)


if __name__ == "__main__":
    s = Solution()
    lst = [1, 2, 3, 4, 1]
    print(s.containsDuplicate(lst))
    print(s.containsDuplicate(list([1, 2, 3, 4])))
