class Solution:
    def getOrder(self, t: List[List[int]]) -> List[int]:
        n = len(t)
        a = [[*task, i] for i, task in enumerate(t)]
        ans = []
        h = []
        i = 0    
        time = 0  

        a.sort()

        while i < n or h:
            if not h:
                time = max(time, a[i][0])
            while i < n and time >= a[i][0]:
                heapq.heappush(h, (a[i][1], a[i][2]))
                i += 1
            p, index = heapq.heappop(h)
            time += p
            ans.append(index)

        return ans

# https://leetcode.com/problems/single-threaded-cpu/description/
