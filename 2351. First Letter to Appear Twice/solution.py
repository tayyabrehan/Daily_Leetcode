class Solution:
    def repeatedCharacter(self, s: str) -> str:
        setS = set()
        for i in s:
            if i in setS:
                return i
            else:
                setS.add(i)