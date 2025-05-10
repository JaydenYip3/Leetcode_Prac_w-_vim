class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        dupes = set()
        longest = 0
        left = 0

        for i in range(len(s)):
            while s[i] in dupes:
                dupes.remove(s[left])
                left += 1
            dupes.add(s[i])
            longest = max(longest, i - left +1)
        
        return longest
                
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("abcad"))


