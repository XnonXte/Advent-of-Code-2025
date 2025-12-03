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
        id_range_split = id_range.split("-")
        id_start_range = int(id_range_split[0])
        id_stop_range = int(id_range_split[1])
        id_int = id_start_range
        while id_int <= id_stop_range:
            id_str = str(id_int)
            id_len = len(id_str)
            # Length of ID needs to be even to compare each halves.
            if id_len % 2 == 0:
                mid_index = id_len // 2
                # Split each halves and compare them.
                if id_str[:mid_index] == id_str[mid_index:]:
                    answer += id_int
            id_int += 1
    return answer


def part_2(data):
    answer = 0
    for id_range in data:
        id_range_split = id_range.split("-")
        id_start_range = int(id_range_split[0])
        id_stop_range = int(id_range_split[1])
        id_int = id_start_range
        while id_int <= id_stop_range:
            id_str = str(id_int)
            id_len = len(id_str)
            # Divide id into several same size chunks.
            for size in range(1, id_len):
                if id_len % size == 0:
                    chunks = [id_str[i : i + size] for i in range(0, id_len, size)]
                    # Check if all the chunks are equal.
                    all_equal = all(x == chunks[0] for x in chunks)
                    if all_equal:
                        answer += id_int
                        break # Only one of the chunk size need to be equal.
            id_int += 1
    return answer


if __name__ == "__main__":
    main()
