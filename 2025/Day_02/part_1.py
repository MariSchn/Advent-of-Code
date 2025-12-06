INPUT_PATH = "2025/Day_02/input.txt"

if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    ranges = []
    for range in lines[0].split(","):
        start, end = map(int, range.split("-"))
        ranges.append((start, end))
 
    # === SOLVE ===
    result = 0
    for start, end in ranges:
        current = start

        while current <= end:
            s = str(current)

            # Odd length numbers can't be a repeated number
            if len(s) % 2 == 1:
                # Start at the smallest number with one more digit
                current = 10 ** len(s) + 1
                continue

            if s[:len(s) // 2] == s[len(s) // 2:]:
                result += current

            current += 1


    # === OUTPUT ===
    print("Sum of all invalid ids: ", result)
