class Solution:
    def totalDigits(self, n: int) -> int:
        total_digits = 0
        length = 1
        start = 1
        
        while start <= n:
            end = start * 10 - 1
            # Number of elements in the current digit range up to n
            count = min(n, end) - start + 1
            
            total_digits += count * length
            
            # Move to the next digit length
            length += 1
            start *= 10
            
        return total_digits
