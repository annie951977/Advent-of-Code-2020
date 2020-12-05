def day2part1(filepath: str) -> int:
    f = open(filepath, "r")
    valid = 0
    content = []

    for line in f:
        x = line.split()
        x[1] = x[1][:1]
        content.append(x)
    for item in content:
        number = 0
        limiters = item[0].split("-")
        min_num = int(limiters[0])
        max_num = int(limiters[1])
        for value in item[2]:
            if value == item[1]:
                number += 1
        if min_num <= number <= max_num:
            valid += 1

    return valid


def day2part2(filepath: str) -> int:
    f = open(filepath, "r")
    valid = 0
    content = []

    for line in f:
        x = line.split()
        x[1] = x[1][:1]
        content.append(x)

    for item in content:
        number = 0
        limiters = item[0].split("-")
        first_pos = int(limiters[0]) -1
        second_pos = int(limiters[1]) -1
        if item[2][first_pos] == item[1] and item[2][second_pos] != item[1]:
            valid += 1
        elif item[2][first_pos] != item[1] and item[2][second_pos] == item[1]:
            valid += 1

    return valid


if __name__ == "__main__":
    print(day2part1("day2.txt"))
    print(day2part2("day2.txt"))
