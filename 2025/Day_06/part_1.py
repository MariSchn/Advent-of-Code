from dataclasses import dataclass, field
from typing import List

INPUT_PATH = "2025/Day_06/input.txt"

@dataclass
class Problem:
    numbers: List[int] = field(default_factory=list)
    operation: str = ""


if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    num_problems = len(list(filter(bool, lines[0].strip().split(" "))))
    problems = [Problem() for _ in range(num_problems)]

    for line in lines[:-1]:
        for i, number in enumerate(filter(bool, line.strip().split(" "))):
            problems[i].numbers.append(int(number))

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