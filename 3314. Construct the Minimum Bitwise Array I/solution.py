class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for n in nums:
            res = -1
            # 0 se n tak check karo, pehla milne wala hi smallest hoga
            for x in range(n):
                if (x | (x + 1)) == n:
                    res = x
                    break
            ans.append(res)
        return ans