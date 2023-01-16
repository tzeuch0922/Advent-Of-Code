# Main
if __name__ == "__main__":
    input_file = open("Day-4-Input.txt", "r")
    line = input_file.readline()
    contain_count = 0
    overlap_count = 0
    while line != "":
        separator = line.index(",")
        dash_one = line.index("-")
        dash_two = line.rindex("-")
        first_start = int(line[:dash_one])
        first_end = int(line[dash_one+1:separator])
        second_start = int(line[separator+1:dash_two])
        second_end = int(line[dash_two+1:])
        if first_start <= second_start and first_end >= second_end or first_start >= second_start and first_end <= second_end:
            contain_count += 1
            overlap_count += 1
        elif not (first_start > second_end or second_start > first_end):
            overlap_count += 1
        line = input_file.readline()
    print("Part 1: " + str(contain_count))
    print("Part 2: " + str(overlap_count))