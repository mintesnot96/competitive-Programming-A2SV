class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []
        for i in range(1, n+1):
            players.append(i)
            
        return self.circularGame(players, k)
    
    
    def circularGame(self, players, k, index = 0):
        if len(players) == 1:
            return players[0]
        
        i = index + k-1
        while i >= len(players):
            i = i - len(players)
            
        players.pop(i)
        if i >= len(players):
            i = i - len(players)
            
        return self.circularGame(players, k, i)


# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
