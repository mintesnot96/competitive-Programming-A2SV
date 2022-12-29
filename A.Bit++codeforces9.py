n=int(input(""))
x=0
for _ in range(0,n):
    s = input()
    if '++' in s:
        x=x+1
    else:
        x=x-1
print(x)

# question link
# https://codeforces.com/problemset/problem/282/A
