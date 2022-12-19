input = [str.strip(l, "\n") for l in open("input_day14.txt","r").readlines()]
input = [str.split(path, " -> ") for path in input]
paths = []
for path in input:
    new_path = [str.split(point, ",") for point in path]
    paths += [[(int(point[0]), int(point[1])) for point in new_path]]

y_len = max([point[1] for path in paths for point in path]) + 1
x_len = max([point[0] for path in paths for point in path]) + 1

grid = [["." for _ in range (0, x_len)] for _ in range(0, y_len)]

for path in paths:
    for i in range(0, len(path)-1):
        start = path[i]
        dest = path[i+1]
        x_diff = dest[0] - start[0]
        y_diff = dest[1] - start[1]
        grid[start[1]][start[0]] = "#"
        for j in range(1, abs(x_diff)+1):
            sign = -1 if x_diff < 0 else 1
            grid[start[1]][int(start[0] + (sign*j))] = "#"
        for k in range(1, abs(y_diff)+1):
            sign = -1 if y_diff < 0 else 1
            grid[int(start[1] + (sign*k))][start[0]] = "#"

def sand_fall(start, ymax):
    if start[1] >= ymax-1:
        return False

    # can go down?
    down = (start[0], start[1]+1)
    
    if grid[down[1]][down[0]] == ".":
        return sand_fall(down, ymax)
    
    down_left = (start[0]-1, start[1]+1)
    if grid[down_left[1]][down_left[0]] == ".":
        return sand_fall(down_left, ymax)
    
    down_right = (start[0]+1, start[1]+1)
    if grid[down_right[1]][down_right[0]] == ".":
        return sand_fall(down_right, ymax)
    
    return start

entry_point = (500, 0)

counter = 0
while True:
    new_position = sand_fall(entry_point, y_len)
    if not new_position:
        print(counter)
        break
    grid[new_position[1]][new_position[0]] = "o"
    counter +=1


# Part 2
y_len = max([point[1] for path in paths for point in path]) + 2
x_len = max([point[0] for path in paths for point in path]) + 500

grid = [["." for j in range (0, x_len)] for _ in range(0, y_len)]

for path in paths:
    for i in range(0, len(path)-1):
        start = path[i]
        dest = path[i+1]
        x_diff = dest[0] - start[0]
        y_diff = dest[1] - start[1]
        grid[start[1]][start[0]] = "#"
        for j in range(1, abs(x_diff)+1):
            sign = -1 if x_diff < 0 else 1
            grid[start[1]][int(start[0] + (sign*j))] = "#"
        for k in range(1, abs(y_diff)+1):
            sign = -1 if y_diff < 0 else 1
            grid[int(start[1] + (sign*k))][start[0]] = "#"

grid += [["#" for i in range(0, x_len)]]

def sand_fall(start, entry_point, ymax):

    # can go down?
    down = (start[0], start[1]+1)
    
    if grid[down[1]][down[0]] == ".":
        return sand_fall(down, entry_point, ymax)
    
    down_left = (start[0]-1, start[1]+1)
    if grid[down_left[1]][down_left[0]] == ".":
        return sand_fall(down_left, entry_point, ymax)
    
    down_right = (start[0]+1, start[1]+1)
    if grid[down_right[1]][down_right[0]] == ".":
        return sand_fall(down_right, entry_point, ymax)
    
    if start == entry_point:
        return False
        
    return start

entry_point = (500, 0)

counter = 1
while True:
    new_position = sand_fall(entry_point, entry_point, y_len)
    if not new_position:
        print(counter)
        break
    grid[new_position[1]][new_position[0]] = "o"
    counter +=1