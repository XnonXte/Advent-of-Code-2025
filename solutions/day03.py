import os

DAY: int = 3  # Fill in the day.


def main() -> None:
    try:
        script_dir: str = os.path.dirname(os.path.abspath(__file__))
        data_path: str = os.path.join(script_dir, "data.txt")
        data: list[str] = read_data(data_path)
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


def part_1(data: list[str]) -> int:
    answer: int = 0
    for bank in data:
        largest_joltage: int = 0
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                joltage = int(bank[i] + bank[j])
                if joltage > largest_joltage:
                    largest_joltage = joltage
        answer += largest_joltage
    return answer


def part_2(data: list[str]) -> int:
    answer: int = 0
    return answer


if __name__ == "__main__":
    main()
