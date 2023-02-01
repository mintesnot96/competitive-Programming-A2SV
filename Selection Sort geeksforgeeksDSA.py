class Solution: 
    def selectionSort(self, arr,n):
        lastindex = n
        k=0
        while lastindex-1>0:
            target = 0
            for i in range(1, lastindex):
                if arr[target]<arr[i]:
                    target = i
            arr[lastindex - 1] , arr[target]=arr[target],arr[lastindex - 1]
            lastindex -= 1
        # print(arr)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends


# https://practice.geeksforgeeks.org/problems/selection-sort/1
