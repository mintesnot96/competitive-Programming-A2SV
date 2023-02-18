tn= int(input())
for i in range(tn):
    n=int(input())
    nlist= list(map(int,input().split()))
    plh=nlist[0]
    sum = 0
    for j in range(len(nlist)):
        if plh*nlist[j]<0:
            sum=sum+plh
            plh=nlist[j]
        if plh<nlist[j]:
           plh= nlist[j]
    sum=sum+plh
    print(sum)
    
#     https://codeforces.com/contest/1343/problem/C
