# 1025. Divisor Game

## Problem Description
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number `n` on the chalkboard. On each player's turn, that player makes a move consisting of:
1. Choosing any integer `x` with `0 < x < n` and `n % x == 0`.
2. Replacing the number `n` on the chalkboard with `n - x`.

If a player cannot make a move, they lose the game.

Return `true` if and only if Alice wins the game, assuming both players play optimally.



## Examples

### Example 1:
**Input:** `n = 2`  
**Output:** `true`  
**Explanation:** - Alice chooses `x = 1` (since $1 < 2$ and $2 \pmod 1 == 0$).
- The number becomes $2 - 1 = 1$.
- Bob cannot choose any `x` such that $0 < x < 1$.
- Bob loses, Alice wins.

### Example 2:
**Input:** `n = 3`  
**Output:** `false`  
**Explanation:** - Alice chooses `x = 1` (the only divisor of 3 less than 3).
- The number becomes $3 - 1 = 2$.
- Bob chooses `x = 1`.
- The number becomes $2 - 1 = 1$.
- Alice has no more moves and loses.

## Constraints:
* `1 <= n <= 1000`