DAY = 0 # Fill in the day


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
    answer = 0
    return answer


if __name__ == "__main__":
    main()