class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        min_y = float('inf')
        max_y = float('-inf')
        
        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
        
        low = min_y
        high = max_y
        
        for _ in range(100):
            mid = (low + high) / 2
            current_below_area = 0
            
            for x, y, l in squares:
                if y >= mid:
                    continue
                elif y + l <= mid:
                    current_below_area += l * l
                else:
                    current_below_area += l * (mid - y)
            
            if current_below_area >= total_area / 2:
                high = mid
            else:
                low = mid
        
        return low