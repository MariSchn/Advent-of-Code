INPUT_PATH = "2025/Day_01/input.txt"

if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    rotations = []
    for line in lines:
        line = line.strip()

        direction = line[0]
        amount = int(line[1:])

        rotations.append((direction, amount))

    # === SOLVE ===
    num_zeros = 0
    current_position = 50
    for direction, amount in rotations:
        if direction == "L":
            current_position -= amount
        elif direction == "R":
            current_position += amount

        current_position = (current_position + 100) % 100

        if current_position == 0:
            num_zeros += 1

    # === OUTPUT ===
    print(f"Number of times at position 0: {num_zeros}")