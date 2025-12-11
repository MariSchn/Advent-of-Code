from dataclasses import dataclass
from typing import List

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


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
        num_buttons = len(machine.buttons)
        num_joltages = len(machine.joltages)

        A = np.zeros((num_joltages, num_buttons))
        for i, button in enumerate(machine.buttons):
            for j in button:
                A[j][i] = 1
        b = np.array(machine.joltages)

        solver_result = milp(
            c=np.ones(num_buttons), 
            constraints=LinearConstraint(A, b, b),
            bounds=Bounds(lb=0, ub=np.inf),
            integrality=np.ones(num_buttons)
        )

        if solver_result.success:
            result += int(round(solver_result.fun))
        
    # === OUTPUT ===
    print(result)