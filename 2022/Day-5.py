import copy

# Main
if __name__ == "__main__":
    input_file = open("Day-5-Input.txt", "r")
    stack_list = []
    for i in range(9):
        stack_list.append([])
    line = input_file.readline()
    while line != "":
        if line.find("[") == -1:
            break
        for i in range(9):
            char = line[4 * i + 1]
            if char != " ":
                stack_list[i].append(char)
        line = input_file.readline()
    for i in range(9):
        stack_list[i].reverse()
    copy_list = copy.deepcopy(stack_list)
    line = input_file.readline()
    line = input_file.readline()
    while line != "":
        move = int(line[5:line.index(" from")])
        from_stack = int(line[line.index(" to")-1:line.index(" to")])-1
        to_stack = int(line[-2:])-1
        line = input_file.readline()
        for i in range(move):
            stack_list[to_stack].append(stack_list[from_stack].pop())
            
        pop_index = len(copy_list[from_stack]) - move
        # print("index: " + str(pop_index) + " length: " + str(len(copy_list[from_stack])))
        
        for i in range(move):
            copy_list[to_stack].append(copy_list[from_stack].pop(pop_index))
    stack_tops = ""
    copy_tops = ""
    for i in range(9):
        stack_tops += str(stack_list[i][-1])
        copy_tops += str(copy_list[i][-1])
    print("Part 1: " + str(stack_tops))
    print("Part 2: " + str(copy_tops))