# Main
if __name__ == "__main__":
    input_file = open("Day-6-Input.txt", "r")
    line = input_file.readline()
    idx = 0
    found = False
    idx2 = 0
    found2 = False
    while True:
        if not found:
            char = line[idx]
            remaining = line[idx + 1:idx + 4]
            for i in range(3):
                if remaining.find(char) != -1:
                    break
                if i == 2:
                    found = True
                    break
                char = remaining[0]
                remaining = remaining[1:]
            if not found:
                idx += 1
        char = line[idx2]
        remaining2 = line[idx2 + 1:idx2 + 14]
        for i in range(13):
            if remaining2.find(char) != -1:
                break
            if i == 12:
                found2 = True
                break
            char = remaining2[0]
            remaining2 = remaining2[1:]
        if found2:
            break
        idx2 += 1
    print("Part 1: " + str(idx+4))
    print("Part 2: " + str(idx2+14))