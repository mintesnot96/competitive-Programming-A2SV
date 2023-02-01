class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if not A or not A[0]:
            return 0
        num_cols, num_rows = len(A[0]), len(A)
        num_remove = 0
        for col_index in range(num_cols):
            for row_index in range(num_rows):
                if row_index > 0 and A[row_index][col_index] < A[row_index-1][col_index]:
                    num_remove += 1
                    break
        return num_remove

      

# https://leetcode.com/problems/delete-columns-to-make-sorted/
