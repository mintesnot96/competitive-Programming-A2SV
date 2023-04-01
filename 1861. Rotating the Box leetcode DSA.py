class Solution:
  def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
    num_rows = len(box)
    num_cols = len(box[0])
    rotated_box = [['.'] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
      k = num_cols - 1
      for j in reversed(range(num_cols)):
        if box[i][j] != '.':
          if box[i][j] == '*':
            k = j
          rotated_box[k][num_rows - i - 1] = box[i][j]
          k -= 1

    return [''.join(row) for row in rotated_box]
# https://leetcode.com/problems/rotating-the-box/description/
