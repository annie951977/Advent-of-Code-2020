## Day 1 of Advent of Code


def day1part1(file: str) -> int:
    f = open(file, "r")
    num_list = []
    for line in f:
        x = int(line.strip())
        num_list.append(x)

    for i in range(len(num_list)):
        for k in range(i+1, len(num_list)):
            if (num_list[i] + num_list[k]) == 2020:
                return num_list[i]*num_list[k]


def day1part2(file: str) -> int:
    f = open(file, "r")
    num_list = []
    for line in f:
        x = int(line.strip())
        num_list.append(x)
    for i in range(len(num_list)):
        for k in range(i+1, len(num_list)):
            for j in range(i+2, len(num_list)):
                if (num_list[i] + num_list[k] + num_list[j]) == 2020:
                    return num_list[i]*num_list[k]*num_list[j]


if __name__ == "__main__":
    print(day1part1("day1.txt"))
    print(day1part2("day1.txt"))
