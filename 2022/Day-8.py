# Main
if __name__ == "__main__":
    input_file = open("Day-8-Input.txt", "r")
    tree_arr = []
    row = 0
    while row < 99:
        line = input_file.readline()
        col = 0
        temp_arr = []
        while col < 99:
            temp_arr.append(int(line[col]))
            col += 1
        tree_arr.append(temp_arr)
        row += 1
            
    visible_count = 0
    max_scenic_score = 0
    for i in range(0,99):
        for j in range(0,99):
            if i == 0 or j == 0 or i == 98 or j == 98:
                visible_count += 1
                continue
            ## check west
            visible = False
            for k in range(0,j):
                if tree_arr[i][j] <= tree_arr[i][(j-1)-k]:
                    score_w = k+1
                    break
                elif k == j-1:
                    score_w = j
                    if not visible:
                        visible = True
                        visible_count += 1
            ## check east
            for k in range(j+1,99):
                if tree_arr[i][j] <= tree_arr[i][k]:
                    score_e = k-j
                    break
                elif k == 98:
                    score_e = 98-j
                    if not visible:
                        visible = True
                        visible_count += 1
            ## check north
            for k in range(0,i):
                if tree_arr[i][j] <= tree_arr[(i-1)-k][j]:
                    score_n = k+1
                    break
                elif k == i-1:
                    score_n = i
                    if not visible:
                        visible = True
                        visible_count += 1
            ## check south
            for k in range(i+1,99):
                if tree_arr[i][j] <= tree_arr[k][j]:
                    score_s = k-i
                    break
                elif k == 98:
                    score_s = 98-i
                    if not visible:
                        visible = True
                        visible_count += 1
            scenic_score = score_s * score_e * score_n * score_w
            if max_scenic_score < scenic_score:
                max_scenic_score = scenic_score
                    
    print("Part 1: " + str(visible_count))
    print("Part 2: " + str(max_scenic_score))