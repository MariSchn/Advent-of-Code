from collections import defaultdict


def task1(left_list, right_list):
    left_list.sort()
    right_list.sort()

    res = 0
    for l, r in zip(left_list, right_list):
        res += abs(l - r)

    return res

def task2(left_list, right_list):
    frequencies = defaultdict(int)

    for r in right_list:
        frequencies[r] += 1

    res = 0
    for l in left_list:
        res += l * frequencies[l]

    return res


if __name__ == '__main__':
    # ===== READ DATA =====
    raw_data = open('input').read().splitlines()

    left_list = []
    right_list = []

    for line in raw_data:
        nums = line.split()
        left_list.append(int(nums[0]))
        right_list.append(int(nums[1]))

    # ===== SOLVE =====
    print(f'Task 1 Solution: {task1(left_list, right_list)}')
    print(f'Task 2 Solution: {task2(left_list, right_list)}')

    
