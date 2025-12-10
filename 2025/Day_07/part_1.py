INPUT_PATH = "2025/Day_07/input.txt"


if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]
    grid = [list(line) for line in lines]

    # === SOLVE ===
    result = 0

    s_idx = grid[0].index("S")
    stack = [(0, s_idx)]

    while stack:
        row, col = stack.pop()

        if grid[row][col] == "|":
            # Cell was already covered by a different beam
            continue
        grid[row][col] = "|" 
        if row == len(grid) - 1:
            # Reached bottom, no need to check next row
            continue

        if grid[row + 1][col] == "^":
            # Beam needs to be split
            result += 1

            if col > 0:
                # Left
                stack.append((row + 1, col - 1))
            if col < len(grid[0]) - 1:
                # Right
                stack.append((row + 1, col + 1))
        else:
            # Beam continues vertically
            stack.append((row + 1, col))

    # === OUTPUT ===
    print(result)