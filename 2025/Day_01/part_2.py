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
        next_position = current_position

        if amount >= 100:
            num_zeros += amount // 100
            amount = amount % 100

        if direction == "L":
            next_position -= amount
        elif direction == "R":
            next_position += amount

        if current_position != 0 and (next_position <= 0 or next_position >= 100):
            num_zeros += 1

        next_position = (next_position + 100) % 100
        current_position = next_position

    # === OUTPUT ===
    print(f"Number of times 0 is passed: {num_zeros}")