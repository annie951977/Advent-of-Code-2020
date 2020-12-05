
def day3part1(filepath: str) -> int:
    tree_count = 0
    width = 3
    with open(filepath) as file:
        file.readline().strip("\n")
        curr_line2 = file.readline().strip("\n")
        while curr_line2 != "":
            if width < len(curr_line2) - 1:
                if curr_line2[width] == "#":
                    tree_count += 1
                width += 3
            else:
                width = width % (len(curr_line2))
                if curr_line2[width] == "#":
                    tree_count += 1
                width += 3
            curr_line2 = file.readline().strip("\n")
    return tree_count


if __name__ == "__main__":
    print(day3part1('day3.txt'))
