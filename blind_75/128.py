class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        hash_set = set(nums)
        longest = 1

        for num in hash_set:
            if num + 1 not in hash_set:
                length = 1

                while (num - length) in hash_set:
                    length += 1
                longest = max(length, longest)
        return longest

print(Solution().longestConsecutive([1,0,1,2]))
print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([1]))
print(Solution().longestConsecutive([0,3,2,7,2,5,8,4,6,0,1]))


