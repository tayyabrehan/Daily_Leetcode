class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        Ans = []
        for i in nums:
            count = 0
            for j in nums:
                if j<i:
                    count +=1
            Ans.append(count)
        return Ans

      #second aproach with sorting
      
       #sorted_n = sorted(nums)
       # result = []
       # for n in nums:
       #     result.append(sorted_n.index(n))
       # return result
            
        