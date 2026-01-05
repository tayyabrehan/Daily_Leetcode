class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_val = float('inf')
        neg_count = 0
        for row in matrix:
            for val in row:
                total_sum += abs(val)
                min_val = min(min_val,abs(val))
                if val < 0:
                    neg_count +=1

        if neg_count % 2==1:
            return total_sum - 2 * min_val
        return total_sum
        