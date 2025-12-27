class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
       # D = 0    
       # for i in range(t):
       #     D -= 2   
       # return num - D
         
        return num+2*t 