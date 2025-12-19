from sys import argv

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
        data = [line.strip() for line in f.readlines()]
        put_beam(data, 1, data[0].index("S"))
        return data


def put_beam(data, row, col):
    data[row] = data[row][:col] + "|" + data[row][col + 1 :]


def part_1(data):
    answer = 0
    for row in range(len(data) - 1):
        for col in range(len(data[row])):
            if data[row][col] == "|":
                if data[row + 1][col] == "^":
                    put_beam(data, row + 1, col - 1)
                    put_beam(data, row + 1, col + 1)
                    answer += 1
                else:
                    put_beam(data, row + 1, col)
    return answer


def part_2(data):
    # TODO: implement part 2
    answer = 0
    return answer


if __name__ == "__main__":
    main()
