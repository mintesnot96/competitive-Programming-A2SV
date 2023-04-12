import math

n = int(input())
for i in range(1, n//2 + 1):
    if i == math.floor(n/2):
        print(i, n-i+1, end="")
    else:
        print(i, n-i+1, end=" ")
if n%2 == 0:
    print()
elif n == 1:
    print("1")
else:
    print("", n//2+1)
    
    
    
# https://codeforces.com/problemset/problem/53/C
