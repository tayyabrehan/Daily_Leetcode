# 804. Unique Morse Code Words 🔡

| Difficulty | Topics | Constraints |
| :---: | :---: | :---: |
| **Easy** | Array, Hash Table, String | $1 \le \text{words.length} \le 100$, $1 \le \text{words}[i].\text{length} \le 12$, letters are lowercase English. |

## 📖 Problem Description

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes.

Given an array of strings `words`, each word can be written as a concatenation of the Morse code of each letter. This concatenation is called the **transformation** of a word.

For example, the word **"cab"** transforms to **`"-.-..--..."`**, which is the concatenation of `"-.-."` ('c'), `".-"` ('a'), and `"-..."` ('b').

The task is to **return the number of different (unique) transformations** among all the words we have.

### 📜 Morse Code Mapping Table

The full mapping for the 26 lowercase letters is:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


## 🚀 Examples

### Example 1:
**Input:** `words = ["gin","zen","gig","msg"]`
**Output:** **2**

**Explanation:**
The transformation of each word is:
* "gin" $\rightarrow$ `"--...-."`
* "zen" $\rightarrow$ `"--...-."`
* "gig" $\rightarrow$ `"--...--."`
* "msg" $\rightarrow$ `"--...--."`
There are 2 different transformations: `"--...-."` and `"--...--."`.

### Example 2:
**Input:** `words = ["a"]`
**Output:** **1**

**Explanation:**
The transformation of "a" is `".-"`. There is 1 unique transformation.
