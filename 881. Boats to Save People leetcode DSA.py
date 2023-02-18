class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people=[3,2,2,1]
        # limit=3
        people.sort()
        i=0
        j=len(people)-1
        boat=0
        # 12345, 3
        while i<=j:
            if people[i]+people[j]<=limit:
                i=i+1
            j=j-1
            boat=boat+1
        return boat
