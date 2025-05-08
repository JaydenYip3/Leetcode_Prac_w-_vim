class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen =  set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


print(Solution().hasDuplicate([1,2,3,4,4]))
print(Solution().hasDuplicate([3,2,4,5,1]))
