class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        for digit1 in num1:
            total *= 10
            localp = 0
            for digit2 in num2:
                localp = localp * 10 + int(digit1) * int(digit2)
            
            product += localp
        
        return str(product)

# qlink https://leetcode.com/problems/multiply-strings/
