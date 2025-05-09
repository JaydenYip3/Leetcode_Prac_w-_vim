class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        hash_s = {}
        hash_t = {}

        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]] = 1 + hash_s[s[i]]
            else:
                hash_s[s[i]] = 1
            if t[i] in hash_t:
                hash_t[t[i]] = 1 + hash_t[t[i]]
            else:
                hash_t[t[i]] = 1
        return hash_s == hash_t


print(Solution().isAnagram("Hello", "World"))
print(Solution().isAnagram("Hello", "elloH"))

