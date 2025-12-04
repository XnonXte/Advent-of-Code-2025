import os
import time

DAY: int = 4  # Fill in the day.
Location = list[list[str]]


def main() -> None:
    try:
        script_dir: str = os.path.dirname(os.path.abspath(__file__))
        data_path: str = os.path.join(script_dir, "data.txt")
        data: Location = [
            list(line) for line in read_data(data_path)
        ]  # Day 4 only fix.
        part_1_answer: int = part_1(data)
        part_2_answer: int = part_2(data)
        print_answers(part_1_answer, part_2_answer)
    except FileNotFoundError:
        print("Data file not found!")
    except Exception as e:
        print(f"Error: {e}")


def print_answers(part_1_answer: int, part_2_answer: int) -> None:
    print("ADVENT OF CODE 2025")
    print("Copyright (C) XnonXte 2025")
    print("=================================================")
    print(f"Day {DAY} answers:")
    print(f"Part 1: {part_1_answer}")
    print(f"Part 2: {part_2_answer}")


def read_data(data_path: str) -> list[str]:
    with open(data_path) as f:
        return [line.strip() for line in f.readlines()]


def check_is_paper(data: Location, i: int, j: int) -> bool:
    try:
        if i < 0 or j < 0:
            return False
        return data[i][j] == "@"
    except IndexError:
        return False


def invert_valid_papers(data: Location) -> tuple[Location, int]:
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


# def visualize_part_2(data: Location):
#     for line in data:
#         for char in line:
#             print(char, end="")
#         print()
#     time.sleep(0.5)
#     os.system("cls")


def part_1(data: Location) -> int:
    answer: int = 0
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


def part_2(data: Location) -> int:
    answer: int = 0
    while True:
        data, total_inverted = invert_valid_papers(data)
        # visualize_part_2(data)
        if total_inverted == 0:
            break
        else:
            answer += total_inverted
    return answer


if __name__ == "__main__":
    main()
