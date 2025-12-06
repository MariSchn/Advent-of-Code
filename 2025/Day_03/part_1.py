INPUT_PATH = "2025/Day_03/input.txt"

if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    banks = [[int(joltage) for joltage in bank.strip()] for bank in lines]

    # === SOLVE ===
    result = 0
    for bank in banks:
        first_max = -1
        second_max = -1

        # Skip last battery to ensure that first_max is never last battery
        for joltage in bank[:-1]:
            if joltage > first_max:
                first_max = joltage
                second_max = -1
            elif joltage > second_max:
                second_max = joltage

        # Manually check if last battery is a higher second_max
        if bank[-1] > second_max:
            second_max = bank[-1]

        result += first_max * 10 + second_max

    # === OUTPUT ===
    print("Maximum joltage possible:", result)
