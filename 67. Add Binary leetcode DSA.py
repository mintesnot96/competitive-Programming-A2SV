# https://leetcode.com/problems/add-binary/description/

def addBinary(a: str, b: str) -> str:
    result = ""
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        sum = carry
        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1
            
        result = str(sum % 2) + result
        carry = sum // 2
        
    return result



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        int_sum = int_a + int_b
        return bin(int_sum)[2:]
      
      
      


      
      
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    ans = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      ans.append(str(carry % 2))
      carry //= 2

    return ''.join(ans[::-1])

				
				
