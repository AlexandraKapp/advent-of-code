# Part 1
input = [str.strip(l, "\n") for l in open("input_day9.txt","r").readlines()]
lines = [str.split(line, " ") for line in input]
movements = [[first, int(second)] for first, second in lines]

start = (0,0)
head_position = start
tail_position = start
has_visited = [tail_position]

for move in movements:
    for steps in range(0, move[1]):
        # move head
        if move[0] == "U":
            head_position = (head_position[0], head_position[1] + 1)
        elif move[0] == "D":
            head_position = (head_position[0], head_position[1] - 1)
        elif move[0] == "R":
            head_position = (head_position[0] + 1, head_position[1])
        elif move[0] == "L":
            head_position = (head_position[0] - 1 , head_position[1])
    
        #move tail
        tail_relative_to_head = (tail_position[0] - head_position[0], 
                                tail_position[1] - head_position[1])

        # same x
        if ((tail_relative_to_head[0] == 0) & (abs(tail_relative_to_head[1])== 2)):
            tail_position = (tail_position[0], tail_position[1] + -1*(tail_relative_to_head[1]/2))
        
        # same y
        if ((tail_relative_to_head[1] == 0) & (abs(tail_relative_to_head[0])== 2)):
            tail_position = (tail_position[0]+ -1*(tail_relative_to_head[0]/2), tail_position[1])

        # diagonal
        elif ((abs(tail_relative_to_head[0]) > 0) & (abs(tail_relative_to_head[1]) > 0) &
            ((abs(tail_relative_to_head[0]) + abs(tail_relative_to_head[1]) >= 3))):
            move_x_direction = 1 if tail_relative_to_head[0] < 0 else -1
            move_y_direction = 1 if tail_relative_to_head[1] < 0 else -1
            tail_position = (tail_position[0] + move_x_direction, tail_position[1] + move_y_direction)

        has_visited += [tail_position]

print(len(set(has_visited)))

# Part 2

start = (0,0)
knots = {i: start for i in range(0, 10)}
has_visited = [start]

def move_head(head_position, move):
    # move head
    if move[0] == "U":
        head_position = (head_position[0], head_position[1] + 1)
    elif move[0] == "D":
        head_position = (head_position[0], head_position[1] - 1)
    elif move[0] == "R":
        head_position = (head_position[0] + 1, head_position[1])
    elif move[0] == "L":
        head_position = (head_position[0] - 1 , head_position[1])
    return (head_position)

def move_tail(head_position, tail_position):
    #move tail
    tail_relative_to_head = (tail_position[0] - head_position[0], 
                            tail_position[1] - head_position[1])

    # same x
    if ((tail_relative_to_head[0] == 0) & (abs(tail_relative_to_head[1])== 2)):
        tail_position = (tail_position[0], tail_position[1] + -1*(tail_relative_to_head[1]/2))
    
    # same y
    if ((tail_relative_to_head[1] == 0) & (abs(tail_relative_to_head[0])== 2)):
        tail_position = (tail_position[0]+ -1*(tail_relative_to_head[0]/2), tail_position[1])

    # diagonal
    elif ((abs(tail_relative_to_head[0]) > 0) & (abs(tail_relative_to_head[1]) > 0) &
        ((abs(tail_relative_to_head[0]) + abs(tail_relative_to_head[1]) >= 3))):
        move_x_direction = 1 if tail_relative_to_head[0] < 0 else -1
        move_y_direction = 1 if tail_relative_to_head[1] < 0 else -1
        tail_position = (tail_position[0] + move_x_direction, tail_position[1] + move_y_direction)

    return(tail_position)

for move in movements:
    for steps in range(0, move[1]):
        knots[0] = move_head(knots[0], move)
        for knot_index in range (1, 10):
            knots[knot_index]= move_tail(knots[knot_index-1], knots[knot_index])
        has_visited += [knots[9]]

print(len(set(has_visited)))