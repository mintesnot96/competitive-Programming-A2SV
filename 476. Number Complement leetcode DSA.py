class Solution:
    def findComplement(self, num: int) -> int:
        num_bits = num.bit_length()
        # or
        num_bits = 0
        n = num
        while n > 0:
            num_bits += 1
            n //= 2

        mask = (1 << num_bits) - 1
        mask=(2 ** num_bits) - 1
        return num^mask
