import os
from sys import argv

DAY = 5  # Fill in the day.


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


def split_data(data):
    # Day 5 only fix.
    try:
        separator = data.index("")
        return data[:separator], data[separator + 1 :]
    except ValueError:
        print("Empty line separator not found in input file!")
        exit(1)


def part_1(data):
    answer = 0
    ranges, ids = split_data(data)
    for id in ids:
        id = int(id)
        for r in ranges:
            r_split = r.split("-")
            start, end = int(r_split[0]), int(r_split[1])
            if id >= start and id <= end:
                answer += 1
                break
    return answer


def part_2(data):
    answer = 0
    id_ranges, _ = split_data(data)
    sorted_id_ranges = sorted(id_ranges, key=lambda r: int(r.split("-")[0]))
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in sorted_id_ranges]
    merged = []
    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    merged.append((current_start, current_end))
    for s, e in merged:
        answer += e - s + 1
    return answer


if __name__ == "__main__":
    main()
