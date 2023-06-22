class Solution:
    def countPrimes(self, num: int) -> int:
        if num <= 2:
            return 0
        
        primes = [True] * num
        primes[0] = primes[1] = False
        
        for i in range(2, int(num**0.5) + 1):
            if primes[i]:
#                 for j in range(i*i, num, i):
                    primes[j] = False
        
        return sum(primes)
      
      
#       https://leetcode.com/problems/count-primes/
