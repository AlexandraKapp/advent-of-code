import string

input = [str.strip(l, "\n") for l in open("input_day12.txt","r").readlines()]
input = [list(line) for line in input]
start = [(input[i].index("S"), i) for i in range(0, len(input)) if "S" in input[i]]
end = [( input[i].index("E"), i) for i in range(0, len(input)) if "S" in input[i]]

height = dict(zip(string.ascii_lowercase[:27], range(1,27)))
height["S"] = 1
height["E"] = 26

def go_to_finish(heads):
    visited_cells = set(start)
    counter = 0
    finished_in = None

    #for i in range(0, 530):
    while finished_in is None:
        counter += 1
        new_heads = set()
        for head in heads:
            head_height = height[input[head[1]][head[0]]]
            up = (head[0], head[1] - 1)
            if (up not in visited_cells) and (up[1] > 0):
                up_letter = input[up[1]][up[0]]
                up_height = height[up_letter]
                if((up_height - head_height )<= 1):
                    if up_letter == "E":
                        finished_in = counter
                    else: 
                        visited_cells.add(up)
                        new_heads.add(up)
            # go down
            down = (head[0], head[1] + 1)
            if down not in visited_cells and (down[1] < len(input)):
                down_letter = input[down[1]][down[0]]
                down_height = height[down_letter]
                if ((down_height - head_height )<= 1):
                    if down_letter == "E":
                        finished_in = counter
                    else: 
                        visited_cells.add(down)
                        new_heads.add(down)

            # go left
            left = (head[0] - 1, head[1])
            if (left not in visited_cells) and (left[0] > 0):
                left_letter = input[left[1]][left[0]]
                left_height = height[left_letter]
                if ((left_height - head_height )<= 1):
                    if left_letter == "E":
                        finished_in = counter
                    else: 
                        visited_cells.add(left)
                        new_heads.add(left)

            # go right
            right = (head[0] + 1, head[1])
            if (right not in visited_cells) and (right[0] < len(input[0])) :
                right_letter = input[right[1]][right[0]]
                right_height = height[right_letter]
                if ((right_height - head_height )<= 1):
                    if right_letter == "E":
                        finished_in = counter
                    else: 
                        visited_cells.add(right)
                        new_heads.add(right)
        heads = new_heads
    print(finished_in)



# Part 1
print("Part 1")
heads = start
go_to_finish(heads)

# Part 2
print("Part 2")
heads = [(input[i].index("a"), i) for i in range(0, len(input)) if "a" in input[i]] + start
go_to_finish(heads)