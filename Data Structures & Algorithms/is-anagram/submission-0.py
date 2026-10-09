class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs_s = {}
        freqs_t = {}
        if len(s) != len(t):
            return False
        for char in s: freqs_s[char] = freqs_s.get(char, 0) + 1
        for char in t: freqs_t[char] = freqs_t.get(char, 0) + 1
        if freqs_s == freqs_t:
            return True
        return False