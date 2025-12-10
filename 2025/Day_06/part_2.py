from dataclasses import dataclass, field
from typing import List

INPUT_PATH = "2025/Day_06/input.txt"

@dataclass
class Problem:
    numbers: List[str] = field(default_factory=list)
    operation: str = ""


if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]

    num_problems = len(list(filter(bool, lines[0].strip().split(" "))))
    numbers_per_problem = len(lines) - 1  # Last line is operations
    problems = [Problem()]

    for c in range(len(lines[0])):
        if all(lines[r][c] == " " for r in range(len(lines) - 1)):
            # Empty column -> New problem
            problem = Problem()
            problem.numbers = ["" for _ in range(numbers_per_problem)]
            problems.append(problem)
            continue

        number = ""
        for r in range(len(lines) - 1):
            char = lines[r][c]
            if char != " ":
                number += char
        problems[-1].numbers.append(number)
    
    for problem in problems:
        problem.numbers = [int(num) for num in problem.numbers if num]

    for i, operation in enumerate(filter(bool, lines[-1].strip().split(" "))):
        problems[i].operation = operation

    # === SOLVE ===
    result = 0

    for problem in problems:
        if problem.operation == "+":
            result += sum(problem.numbers)
        elif problem.operation == "*":
            product = 1
            for number in problem.numbers:
                product *= number
            result += product
        else:
            raise ValueError(f"Found invalid operation '{problem.operation}'. Operation should either be  '+' or '*'")

    # === OUTPUT ===
    print(result)