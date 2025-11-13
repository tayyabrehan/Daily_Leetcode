class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
             ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
             "...","-","..-","...-",".--","-..-","-.--","--.."]
        unique = set()
        for word in words:
            morse_word = ""
            for ch in word:
                morse_word += morse[ord(ch) - ord('a')]
            unique.add(morse_word)
        
        return len(unique)
        