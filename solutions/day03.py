from sys import argv

DAY = 3  # Fill in the day.


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


def part_1(data):
    answer = 0
    for bank in data:
        largest_joltage: int = 0
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                joltage = int(bank[i] + bank[j])
                if joltage > largest_joltage:
                    largest_joltage = joltage
        answer += largest_joltage
    return answer


def part_2(data):
    def max_subseq_12(bank):
        n = len(bank)
        if n < 12:
            return 0
        need = 12
        start = 0
        result_digits = []
        for rem in range(need, 0, -1):
            max_digit = None
            max_idx = -1
            upper = n - rem + 1
            for i in range(start, upper):
                d = bank[i]
                if (max_digit is None) or (d > max_digit):
                    max_digit = d
                    max_idx = i
                    if max_digit == "9":
                        break
            result_digits.append(max_digit)
            start = max_idx + 1
        return int("".join(result_digits))

    answer = 0
    for bank in data:
        largest_joltage = max_subseq_12(bank)
        answer += largest_joltage
    return answer


if __name__ == "__main__":
    main()
