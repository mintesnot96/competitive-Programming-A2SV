n,k = map(int,input().split())
l = sorted(list(map(int,input().split())))
a = [1] + l
print(a[k] if k == n or a[k + 1] - a[k] else -1)
