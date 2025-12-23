class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        while mn:
            mn, mx = mx % mn,mn
        return mx
