class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i, c in enumerate(s):
        #     if s.count(c) == 1:
        #         return i
        # return -1

        d = Counter(s)
        for i, c in enumerate(s):
            if d[c] == 1:
                return i 
        return -1
