## Day 1 of Advent of Code


def day1(file: str) -> int:
    f = open(file, "r")
    num_list = []
    for line in f:
        x = int(line.strip())
        num_list.append(x)

    for i in range(len(num_list)):
        for k in range(i+1, len(num_list)):
            if (num_list[i] + num_list[k]) == 2020:
                return num_list[i]*num_list[k]


if __name__ == "__main__":
    print(day1("day1.txt"))
