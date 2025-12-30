class Solution:
    def countSegments(self, s: str) -> int:
        #with out loop and one line
        #return len(s.split()) 
        
        #solution with loop
        count = 0
        word = s.split()
        for words in word:
            count +=1
        return count