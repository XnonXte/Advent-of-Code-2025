import os

DAY = 0  # Fill in the day.


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
    except Exception as e:
        print(f"Error: {e}")


def solution(data):
    return part_1(data), part_2(data)


def part_1(data):
    # TODO: implement part 1
    return None


def part_2(data):
    # TODO: implement part 2
    return None


if __name__ == "__main__":
    main()
