def findMinDifference(timePoints):
    minutes = []
    for time in timePoints:
        hour, minute = time.split(':')
        minutes.append(int(hour) * 60 + int(minute))
    minutes.sort()
    min_difference = float('inf')
    for i in range(len(minutes) - 1):
        min_difference = min(min_difference, minutes[i + 1] - minutes[i])
    min_difference = min(min_difference, 1440 - (minutes[-1] - minutes[0]))
    return min_difference
# or

# class Solution(object):
#     def findMinDifference(self, timePoints):
        
#         minutes = [60 * int(time[:2]) + int(time[3:]) for time in timePoints]
#         minutes.sort()
#         return min(
#             (y - x) % 1440
#             for x, y in zip(minutes, minutes[1:] + minutes[:1])
#         )
