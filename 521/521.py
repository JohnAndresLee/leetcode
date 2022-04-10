class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        len1, len2 = len(a), len(b)
        if len1 != len2:
            return max(len1, len2)
        else:
            if a == b:
                return -1
            else:
                return len1