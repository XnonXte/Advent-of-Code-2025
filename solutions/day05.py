import os
from sys import argv

DAY: int = 5  # Fill in the day.


def main() -> None:
    try:
        if len(argv) != 2:
            print("Usage: day<number>.py <input_path>")
            return
        data: list[str] = read_data(argv[1])
        part_1_answer: int = part_1(data)
        part_2_answer: int = part_2(data)
        print_answers(part_1_answer, part_2_answer)
    except FileNotFoundError:
        print("Input file not found!")
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


def split_data(data: list[str]) -> tuple[list[str], list[str]]:
    # Day 5 only fix.
    try:
        separator = data.index("")
        return data[:separator], data[separator + 1 :]
    except ValueError:
        print("Empty line separator not found in input file!")
        exit(1)


def part_1(data: list[str]) -> int:
    answer: int = 0
    fresh_id_ranges, ids = split_data(data)
    for id in ids:
        id = int(id)
        for fresh_id_range in fresh_id_ranges:
            id_range_split = fresh_id_range.split("-")
            start, end = int(id_range_split[0]), int(id_range_split[1])
            if id >= start and id <= end:
                answer += 1
                break
    return answer


def part_2(data: list[str]) -> int:
    # TODO: implement part 2
    answer: int = 0
    return answer


if __name__ == "__main__":
    main()
