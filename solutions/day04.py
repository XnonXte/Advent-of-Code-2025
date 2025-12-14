import os
import time
from sys import argv

DAY = 4  # Fill in the day.
Location = list


def main():
    try:
        if len(argv) != 2:
            print("Usage: day<number>.py <input_path>")
            return
        data_path = argv[1]
        data = [list(line) for line in read_data(data_path)]  # Day 4 only fix.
        part_1_answer = part_1(data)
        part_2_answer = part_2(data)
        print_answers(part_1_answer, part_2_answer)
    except FileNotFoundError:
        print("Input file not found!")
    except Exception as e:
        print(f"Error: {e}")


def print_answers(part_1_answer, part_2_answer):
    print("ADVENT OF CODE 2025")
    print("Copyright (C) XnonXte 2025")
    print("=================================================")
    print(f"Day {DAY} answers:")
    print(f"Part 1: {part_1_answer}")
    print(f"Part 2: {part_2_answer}")


def read_data(data_path):
    with open(data_path) as f:
        return [line.strip() for line in f.readlines()]


def check_is_paper(data, i, j):
    try:
        if i < 0 or j < 0:
            return False
        return data[i][j] == "@"
    except IndexError:
        return False


def invert_valid_papers(data):
    total_inverted = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@":
                adjecent_indexes = [
                    [i + 1, j],
                    [i, j + 1],
                    [i - 1, j],
                    [i, j - 1],
                    [i + 1, j - 1],
                    [i - 1, j + 1],
                    [i + 1, j + 1],
                    [i - 1, j - 1],
                ]
                if (
                    sum(list(check_is_paper(data, i, j) for i, j in adjecent_indexes))
                    < 4
                ):
                    data[i][j] = "."
                    total_inverted += 1
    return data, total_inverted


def visualize_part_2(data):
    for line in data:
        for char in line:
            print(char, end="")
        print()
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")


def part_1(data):
    answer = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@":
                adjecent_indexes = [
                    [i + 1, j],
                    [i, j + 1],
                    [i - 1, j],
                    [i, j - 1],
                    [i + 1, j - 1],
                    [i - 1, j + 1],
                    [i + 1, j + 1],
                    [i - 1, j - 1],
                ]
                if (
                    sum(list(check_is_paper(data, i, j) for i, j in adjecent_indexes))
                    < 4
                ):
                    answer += 1
    return answer


def part_2(data):
    answer = 0
    while True:
        data, total_inverted = invert_valid_papers(data)
        visualize_part_2(data)
        if total_inverted == 0:
            break
        else:
            answer += total_inverted
    return answer


if __name__ == "__main__":
    main()
