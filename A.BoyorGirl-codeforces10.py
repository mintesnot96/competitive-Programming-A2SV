
s=input("")
w=''
for c in s:
    if c not in w:
        w=w+c
count=len(w)

print('CHAT WITH HER!') if count%2==0 else print('IGNORE HIM!')

# question link
# https://codeforces.com/problemset/status?my=on
