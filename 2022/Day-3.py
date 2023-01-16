def priority_to_int(item):
    item_ascii = ord(item)
    if item_ascii > 96:
        return item_ascii - 96
    else:
        return item_ascii - 38

# Main
if __name__ == "__main__":
    input_file = open("Day-3-Input.txt", "r")
    priority_sum = 0
    line = input_file.readline()
    while line != "":
        i = 0
        half = (len(line)//2)
        second_half = line[half:]
        while i < half:
            char = line[i]
            if second_half.find(char) != -1:
                break
            i += 1
        priority_sum += priority_to_int(char)
        line = input_file.readline()
    input_file.close()
    input_file = open("Day-3-Input.txt", "r")
    triple_sum = 0
    line_one = input_file.readline()
    line_two = input_file.readline()
    line_three = input_file.readline()
    while True:
        i = 0
        while True:
            char = line_one[i]
            if line_two.find(char) != -1 and line_three.find(char) != -1:
                triple_sum += priority_to_int(char)
                break
            i += 1
        line_one = input_file.readline()
        if line_one == "":
            break
        line_two = input_file.readline()
        line_three = input_file.readline()
    print("Part 1: " + str(priority_sum))
    print("Part 2: " + str(triple_sum))