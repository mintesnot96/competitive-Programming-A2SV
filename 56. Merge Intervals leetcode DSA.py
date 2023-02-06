class Solution:
    def merge(self, input_intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(input_intervals, key=lambda x:x[0])
        merged_intervals = []
        for interval in sorted_intervals:
            current_interval = interval
            if merged_intervals:
                if merged_intervals[-1][1] >= interval[0]: 
                    current_interval = merged_intervals.pop()
                    if interval[1] > current_interval[1]:
                        current_interval[1] = interval[1]      
            merged_intervals.append(current_interval)
        return merged_intervals
