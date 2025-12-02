import os

DAY = 2  # Fill in the day.


def main():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_dir, "data.txt")

        with open(data_path) as f:
            data = [line.strip() for line in f.readlines()]

            print("ADVENT OF CODE 2025")
            print("Copyright (C) XnonXte 2025")
            print("=================================================")

            part_1_answer, part_2_answer = solution(data)

            print(f"Day {DAY} answers:")
            print(f"Part 1: {part_1_answer}")
            print(f"Part 2: {part_2_answer}")

    except FileNotFoundError:
        print("Data file not found!")


def solution(data):
    # Day 2 only fix.
    data = [id_range for id_range in data[0].split(",")]
    return part_1(data), part_2(data)


def part_1(data):
    answer = 0
    for id_range in data:
        floor = int(id_range.split("-")[0])
        ceil = int(id_range.split("-")[1])
        current_id = floor
        while current_id <= ceil:
            current_id_str = str(current_id)
            if len(current_id_str) % 2 == 0:
                mid_index = len(current_id_str) // 2
                if current_id_str[:mid_index] == current_id_str[mid_index:]:
                    answer += current_id
            current_id += 1
    return answer


def part_2(data):
    answer = 0
    return answer


if __name__ == "__main__":
    main()
