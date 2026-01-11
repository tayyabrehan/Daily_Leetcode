class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low, high = 0, len(s)
        perm = []
        for ch in s:
            if ch == 'I':
                perm.append(low)
                low += 1
            else: #D
                perm.append(high)
                high -= 1
        perm.append(low)
        return perm