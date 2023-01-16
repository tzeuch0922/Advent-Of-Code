# Convert values
def convert_input_to_int(choice):
    # Rock
    if choice == "X" or choice == "A":
        return 1
    # Paper
    elif choice == "Y" or choice == "B":
        return 2
    # Scissors
    else:
        return 3
    
# Main
if __name__ == "__main__":
    my_score_part_1 = 0
    my_score_part_2 = 0
    input_file = open("Day-2-Input.txt", "r")
    line = input_file.readline()
    while line != "":
        op_choice = convert_input_to_int(line[0])
        my_choice = convert_input_to_int(line[2])
        
        # Part 1 Calculation
        my_score_part_1 += my_choice
        # Tie
        if my_choice == op_choice:
            my_score_part_1 += 3
        # Win
        elif (my_choice-op_choice) % 3 == 1:
            my_score_part_1 += 6
        
        # Part 2 Calculation
        my_score_part_2 += (my_choice - 1) * 3 + (1 + ((op_choice - 1) - (2 - (my_choice))) % 3)
        
        line = input_file.readline()
    print("Part 1: " + str(my_score_part_1))
    print("Part 2: " + str(my_score_part_2))