# 2140. Solving Questions With Brainpower

## Problem Description
You are given a 0-indexed 2D integer array `questions` where `questions[i] = [points_i, brainpower_i]`. 

You must process questions in order, choosing to either:
- **Solve** question `i`: Earn `points_i` but skip the next `brainpower_i` questions
- **Skip** question `i`: Move to the next question with no penalty

Return the **maximum points** you can earn.

### Examples
**Example 1:**  
Input: `questions = [[3,2],[4,3],[4,4],[2,5]]`  
Output: `5`  
Explanation: Solve Q0 (3 pts, skip Q1-2) + Q3 (2 pts) = 5 pts

**Example 2:**  
Input: `questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]`  
Output: `7`  
Explanation: Skip Q0 → Solve Q1 (2 pts, skip Q2-3) + Q4 (5 pts) = 7 pts
