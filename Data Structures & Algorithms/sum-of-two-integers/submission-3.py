class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (b & mask) != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        # Handle Python's infinite precision for negative results
        return (a & mask) if b > 0 else a