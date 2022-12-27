# A bit brute force. There MUST be a more elegant and concise way to do this.

import sys

import numpy as np

INPUT = "input.txt"

class Forest:
    def __init__(self, trees):
        self.trees = trees
        self.num_rows, self.num_cols = self.trees.shape

    def scenic_score(self, row, col):
        if (row == 0) or (col == 0):
            # First row/column
            return 0
        if (row == (self.num_rows - 1)) or (col == (self.num_cols - 1)):
            # Last row/column
            return 0

        # Check left
        left_score = 1
        col_index = col - 1
        while (col_index != 0) and (self.trees[row][col_index] < self.trees[row][col]):
            col_index -= 1
            left_score += 1

        # Check right
        right_score = 1
        col_index = col + 1
        while (col_index < self.num_cols - 1) and (self.trees[row][col_index] < self.trees[row][col]):
            col_index += 1
            right_score += 1

        # Check down
        down_score = 1
        row_index = row + 1
        while (row_index < self.num_rows - 1) and (self.trees[row_index][col] < self.trees[row][col]):
            row_index += 1
            down_score += 1

        # Check up
        up_score = 1
        row_index = row - 1
        while (row_index != 0) and (self.trees[row_index][col] < self.trees[row][col]):
            row_index -= 1
            up_score += 1

        return (left_score * right_score * up_score * down_score)

forest = Forest(np.genfromtxt(INPUT, delimiter=1, dtype=int))
scenic = np.zeros((forest.num_rows, forest.num_cols), dtype=int)
for row in range(forest.num_rows):
    for col in range(forest.num_cols):
        scenic[row][col] = forest.scenic_score(row, col)

print(f"Highest scenic score possible = {np.max(scenic)}")
