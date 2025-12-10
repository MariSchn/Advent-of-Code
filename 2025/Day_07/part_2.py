from collections import defaultdict

INPUT_PATH = "2025/Day_07/input.txt"

class Node:
    left = None
    right = None

    def is_leaf(self) -> bool:
        return self.left == None and self.right == None


if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]
    grid = [list(line) for line in lines]

    # === SOLVE ===
    result = 0

    s_idx = grid[0].index("S")
    active_cols = defaultdict(int)
    active_cols[s_idx] = 1

    for row in grid:
        for col, cell in enumerate(row):
            if cell == "^":
                if col > 0:
                    # Left
                    active_cols[col - 1] += active_cols[col]
                if col < len(grid[0]) - 1:
                    # Right
                    active_cols[col + 1] += active_cols[col]

                active_cols[col] = 0

    result = sum(list(active_cols.values()))

    # === OUTPUT ===
    print(result)