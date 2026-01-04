class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            divs = []
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divs.append(i)
                    if i*i != n: 
                        divs.append(n // i)
                
                if len(divs) > 4: break
            
            if len(divs) == 4:
                total += sum(divs)
        return total