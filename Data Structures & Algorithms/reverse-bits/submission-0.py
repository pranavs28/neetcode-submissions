class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = ["0"] * 32
        i = 0
        for bit in bin(n)[2:][::-1]:
            binary_str[i] = bit
            i += 1
        return int("".join(binary_str), 2)
        