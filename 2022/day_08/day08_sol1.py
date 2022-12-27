# A bit brute force. There MUST be a more elegant and concise way to do this.

import sys

import numpy as np

INPUT = "input.txt"

class Forest:
    def __init__(self, trees):
        self.trees = trees
        self.num_rows, self.num_cols = self.trees.shape

    def is_visible(self, row, col):
        if (row == 0) or (col == 0):
            # First row/column
            return True
        if (row == (self.num_rows - 1)) or (col == (self.num_cols - 1)):
            # Last row/column
            return True

        # Check left
        if self.trees[row][col] > max(self.trees[row][0:col]):
            return True

        # Check right
        if self.trees[row][col] > max(self.trees[row][col + 1:]):
            return True

        # Check up
        if self.trees[row][col] > max(self.trees[0:row, col]):
            return True

        # Check down
        if self.trees[row][col] > max(self.trees[row + 1:, col]):
            return True

        return False

forest = Forest(np.genfromtxt(INPUT, delimiter=1, dtype=int))
visible = np.zeros((forest.num_rows, forest.num_cols), dtype=int)
for row in range(forest.num_rows):
    for col in range(forest.num_cols):
        visible[row][col] = forest.is_visible(row, col)
print(f"Number of trees visible from outside grid = {np.sum(visible)}")
