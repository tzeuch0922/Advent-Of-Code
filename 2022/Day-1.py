if __name__ == "__main__":
    elf_calorie_arr = []
    calorie_count = 0
    max_1 = 0
    max_2 = 0
    max_3 = 0
    with open("Day-1-Input.txt") as input_file:
        while True:
            line = input_file.readline()
            # if line has content
            if line.strip():
                calorie_count += int(line.strip())
            # else line is empty
            else:
                elf_calorie_arr.append(calorie_count)
                calorie_count = 0
                
            if line[-1:] != '\n':
                break    
    
    for count in elf_calorie_arr:
        if count > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = count
        elif count > max_2:
            max_3 = max_2
            max_2 = count
        elif count > max_3:
            max_3 = count
    print("Day 1 Challenge 1")
    print("Total calories from elf with most calories: " + str(max_1))
    print()
    new_max = max_1 + max_2 + max_3
    print("Day 2 Challenge 2")
    print("Total calories from top 3 elves with most calories: " + str(new_max))