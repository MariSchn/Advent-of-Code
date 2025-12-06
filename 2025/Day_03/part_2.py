INPUT_PATH = "2025/Day_03/input.txt"

if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    banks = [[int(joltage) for joltage in bank.strip()] for bank in lines]

    # === SOLVE ===
    result = 0
    for bank in banks:
        maximums = []
        current_start = 0

        for digit in range(11, -1, -1):
            valid_batteries = bank[current_start:(-digit or len(bank))]
            maximum = max(valid_batteries)
            
            current_start += valid_batteries.index(maximum) + 1
            maximums.append(maximum)

        result += int("".join([str(battery) for battery in maximums]))

    # === OUTPUT ===
    print("Maximum joltage possible:", result)
