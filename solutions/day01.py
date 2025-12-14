from sys import argv

DAY = 1  # Fill in the day.


def main():
    try:
        if len(argv) != 2:
            print("Usage: day<number>.py <input_path>")
            return
        data = read_data(argv[1])
        print("ADVENT OF CODE 2025")
        print("Copyright (C) XnonXte 2025")
        print("=================================================")
        part_1_answer, part_2_answer = solution(data)
        print(f"Day {DAY} answers:")
        print(f"Part 1: {part_1_answer}")
        print(f"Part 2: {part_2_answer}")
    except FileNotFoundError:
        print("Input file not found!")
    except Exception as e:
        print(f"Error: {e}")


def solution(data):
    return part_1(data), part_2(data)


def read_data(data_path):
    with open(data_path) as f:
        return [line.strip() for line in f.readlines()]


def part_1(data):
    # Same as part 2 but without checking if the dial points at 0 at any given rotation.
    answer = 0
    dial = 50
    for i in range(len(data)):
        instruction = data[i]
        rotation = int(instruction[1:])
        if instruction[0] == "L":
            remaining_rotation = rotation
            while remaining_rotation > 0:
                dial -= 1
                remaining_rotation -= 1
                if dial < 0:
                    dial = 99
            if dial == 0:
                answer += 1
        elif instruction[0] == "R":
            remaining_rotation = rotation
            while remaining_rotation > 0:
                dial += 1
                remaining_rotation -= 1
                if dial > 99:
                    dial = 0
            if dial == 0:
                answer += 1
    return answer


def part_2(data):
    answer = 0
    dial = 50
    for i in range(len(data)):
        instruction = data[i]
        rotation = int(instruction[1:])
        if instruction[0] == "L":
            # Store the remaining rotation after each dial.
            remaining_rotation = rotation
            point_at_0 = 0
            while remaining_rotation > 0:
                # Store how many time(s) the dial point at 0.
                if dial == 0:
                    point_at_0 += 1
                dial -= 1
                remaining_rotation -= 1
                # If the dial excedeed the left-most dial.
                if dial < 0:
                    dial = 99
            answer += point_at_0
        elif instruction[0] == "R":
            # Same procedure as the left rotation just to the right.
            remaining_rotation = rotation
            point_at_0 = 0
            while remaining_rotation > 0:
                if dial == 0:
                    point_at_0 += 1
                dial += 1
                remaining_rotation -= 1
                # If the dial excedeed the right-most dial.
                if dial > 99:
                    dial = 0
            answer += point_at_0
    return answer


if __name__ == "__main__":
    main()
