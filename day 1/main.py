DAY = 1  # Fill in the day.


def main():
    try:
        with open("./data.txt") as f:
            data = [line.replace("\n", "") for line in f.readlines()]
            print("ADVENT OF CODE 2025")
            print("Copyright (C) XnonXte 2025")
            print("=================================================")
            answer = solution(data)
            print(f"Day {DAY} Answer: {answer}")
    except FileNotFoundError:
        print("Data file not found!")


def solution(data):
    count = 0
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
            count += point_at_0
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
            count += point_at_0
    return count


if __name__ == "__main__":
    main()
