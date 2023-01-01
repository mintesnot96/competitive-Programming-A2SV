class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big -= 1
            return self.big >= 0
        elif carType == 2:
            self.medium -= 1
            return self.medium >= 0
        elif carType == 3:
            self.small -= 1
            return self.small >= 0
        else:
            return False
# Question link
# https://leetcode.com/problems/design-parking-system/description/
