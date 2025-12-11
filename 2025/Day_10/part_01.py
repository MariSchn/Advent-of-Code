from dataclasses import dataclass
from itertools import combinations
from typing import List


INPUT_PATH = "2025/Day_10/input.txt"

@dataclass
class Machine:
    target: List[bool]
    buttons: List[List[int]]
    joltages: List[int]


def test_buttons(buttons, target):
    current = [False for _ in range(len(target))]

    for button in buttons:
        for idx in button:
            current[idx] = not current[idx]

    if current == target:
        return True
    
    return False


if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    machines = []
    for line in lines:
        parts = line.split(" ")

        joltages = list(map(int, parts[-1][1:-1].split(",")))

        target = []
        for light in parts[0][1:-1]:
            target.append(True if light == "#" else False)

        buttons = []
        for button in parts[1:-1]:
            buttons.append(list(map(int, button[1:-1].split(","))))

        machines.append(Machine(target, buttons, joltages))

    # === SOLVE ===
    result = 0

    for machine in machines:
        num_lights = len(machine.target)

        found = False
        for i in range(1, len(machine.buttons)):
            for pressed in combinations(machine.buttons, i):
                if test_buttons(pressed, machine.target):
                    found = True
                    break

            if found:
                result += i
                break

    # === OUTPUT ===
    print(result)