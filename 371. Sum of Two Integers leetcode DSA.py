# https://leetcode.com/problems/sum-of-two-integers/description/
class Solution {
    public int getSum(int a, int b) {
        while (b!=0){
            int temp= (a & b) <<1;
            a=(a^b);
            b=temp;
    }
        return a;
        
    }
}

# pyhon
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7fffffff else ~(a ^ mask)
				
				
				

class Solution:
    def getSum(self, a: int, b: int) -> int:
        n=0xffffffff
        while (b & n)>0:
            temp= (a & b) <<1
            a=(a^b)
            b=temp
        return (a & n) if b>0 else a
				
				
				
				

