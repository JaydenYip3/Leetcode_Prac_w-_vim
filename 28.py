class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
       
        length_needle = len(needle)
        length_haystack = len(haystack)

        if length_needle > length_haystack: 
            return -1
        for index in range(length_haystack):
            if haystack[index: index + length_needle] == needle:
                return index
        return -1


            
print(Solution().strStr("sadbutsad", "sad"))
print(Solution().strStr("sadbutsad", "but"))
print(Solution().strStr("","NotFound"))
print(Solution().strStr("Hello", "Hello"))
