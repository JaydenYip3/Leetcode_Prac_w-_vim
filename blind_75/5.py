class Solution:
    def longestPalindrome(self, s: str) -> str: 
        if len(s) <= 1:
            return s 
        longest = 0
        longest_word = ""
        for index in range(1, len(s)):
            w1 = self.evenPalindrome(s, index)
            w2 = self.oddPalindrome(s, index)
            longest= max(longest, len(w1), len(w2))
            if len(w1) == longest:
                longest_word = w1
            elif len(w2) == longest:
                longest_word = w2
        return longest_word

            
    def evenPalindrome(self, s:str, mid: int) -> str:
        left = mid - 1
        right = mid

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        else:
            return s[left + 1:right]
    
    def oddPalindrome(self, s:str, mid: int) -> str:
        left = mid - 1
        right = mid + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        else:
            return s[left + 1:right]

print(Solution().evenPalindrome("baab", 0))
print(Solution().evenPalindrome("baab", 1))
print(Solution().evenPalindrome("baab", 2))
print(Solution().evenPalindrome("baab", 3))
print(Solution().oddPalindrome("aba", 1))
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
