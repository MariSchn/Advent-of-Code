INPUT_PATH = "2025/Day_04/input.txt"

OFFSETS = [(-1, -1), (-1,  0), (-1,  1),
           ( 0, -1),           ( 0,  1),
           ( 1, -1), ( 1,  0), ( 1,  1)]

if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    grid = [[cell == "@" for cell in line.strip()] for line in lines]

    # === SOLVE ===
    result = 0

    num_rows = len(grid)
    num_cols = len(grid[0])

    for r in range(num_rows):
        for c in range(num_cols):
            if not grid[r][c]:
                continue

            num_adjacent = 0

            for dr, dc in OFFSETS:
                updated_r = r + dr
                updated_c = c + dc

                if not (0 <= updated_r < num_rows) or not (0 <= updated_c < num_cols):
                    continue
                
                if grid[updated_r][updated_c]:
                    num_adjacent += 1


            if num_adjacent < 4:
                result += 1

    # === OUTPUT ===
    print("Number of accessible rolls of paper:", result)
