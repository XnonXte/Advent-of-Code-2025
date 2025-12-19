from sys import argv
import math

FILE_NAME = __file__.split("\\")[-1]
DAY = FILE_NAME[3:5]

def main():
    try:
        if len(argv) != 2:
            print("Usage: day<number>.py <input_path>")
            return
        data = read_data(argv[1])
        part_1_answer = part_1(data)
        part_2_answer = part_2(data)
        print_answers(part_1_answer, part_2_answer)
    except FileNotFoundError:
        print("Input file not found!")


def print_answers(part_1_answer, part_2_answer):
    print("ADVENT OF CODE 2025")
    print("Copyright (C) XnonXte 2025")
    print("=================================================")
    print(f"Day {DAY} answers:")
    print(f"Part 1: {part_1_answer}")
    print(f"Part 2: {part_2_answer}")


def read_data(data_path):
    # Day 6 fix
    with open(data_path) as f:
        return [line.replace("\n", "") + " " for line in f.readlines()]


def calc_total(numbers_set):
    total = 0
    for line in numbers_set:
        operator = line[-1]
        numbers = [int(n) for n in line[:-1]]
        match operator:
            case "+":
                total += sum(numbers)
            case "*":
                total += math.prod(numbers)
    return total


def part_1(data):
    answer = 0
    numbers_set = [line.split() for line in data]
    numbers_set_t = list(map(list, zip(*numbers_set)))
    answer = calc_total(numbers_set_t)
    return answer


def part_2(data):
    answer = 0
    numbers_set = []
    numbers = []
    rows = len(data) - 1
    for col in range(len(data[0])):
        number = [data[row][col] for row in range(rows)]
        operator = data[rows][col]
        if operator in ["*", "+"]:
            numbers.append(operator)
        if "".join(number) == " " * (rows):
            numbers_set.append(numbers)
            numbers = []
        else:
            numbers.insert(-1, int("".join(number).strip()))
    answer = calc_total(numbers_set)
    return answer


if __name__ == "__main__":
    main()
