class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        S = set()
        if (s1 == s2):
            return True
        if (len(s1) != len(s2)):
            return False
        if (sorted(s1) != sorted(s2)):
            return False
        if (s1, s2) in S:
            return True
        length = len(s1)
        for i in range(length - 1):
            if self.isScramble(s1[: i + 1], s2[: i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:]):
                S.add((s1,s2))
                S.add((s2,s1))
                return True
            if self.isScramble(s1[: i + 1], s2[length - 1 - i:]) and self.isScramble(s1[i + 1:], s2[: length - 1 - i]):
                S.add((s1,s2))
                S.add((s2,s1))
                return True
        
        return False

s1 = "abc"
s2 = "bca"
test = Solution()
print(test.isScramble(s1, s2))