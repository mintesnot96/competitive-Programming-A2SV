
class Solution:
    def average(self, salary: List[int]) -> float:
        A = sorted(salary, reverse=True)
        sum=0
        print(A)
        for i in range(1,len(A)-1,1):
            sum = sum+A[i]
        print(len(A)-2)
        print(sum)
        return sum/(len(A)-2)


# qlink https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/?
