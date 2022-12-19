import numpy as np
from shapely import geometry

# Part 1
print("part 1")

y_query = 2000000

def manhattan_distance(a, b):
    return (abs(a[0]-b[0]) + abs(a[1]-b[1]))

filecontent = [str.strip(l, "\n") for l in open("input_day15.txt","r").readlines()]
filecontent = [str.split(line, "Sensor at x=")[1] for line in filecontent]
filecontent = [str.split(line, ", y=") for line in filecontent]
filecontent = [[line[0], str.split(line[1], ": closest beacon is at x="), line[2]] for line in filecontent]
filecontent = [[int(line[0]), int(line[1][0]), int(line[1][1]), int(line[2])] for line in filecontent]

# shift minimum value of x to 0 if < 0, otherwise array indexing doesnt work
max_x_grid = max([line[0] + manhattan_distance(line[0:2], line[2:]) for line in filecontent])
min_x_grid = min([line[0] - manhattan_distance(line[0:2], line[2:]) for line in filecontent])
if min_x_grid < 0:
    input = [[line[0] - min_x_grid, line[1], \
                line[2] - min_x_grid, line [3]] for line in filecontent]
    max_x_grid = max_x_grid - min_x_grid
    min_x_grid = 0

y_query_row = np.repeat(".", max_x_grid)

for line in input:
    md = manhattan_distance(line[0:2], line[2:])
    for i in range(0, md):
        if ((line[1] + i) == y_query) | ((line[1] - i) == y_query):
            y_query_row[line[0] - (md-i):line[0] + (md-i)] = "#"

print(sum(y_query_row != "."))

# Part 2:
print("part 2")
max_coord = 4000000 
input = filecontent

poly = geometry.Polygon()

for line in input:
    md = manhattan_distance(line[0:2], line[2:])
    poly = poly.union(geometry.Polygon([(line[0]-md, line[1]), (line[0], line[1]-md), (line[0]+md, line[1]), (line[0], line[1]+md)]))

target_search_area = geometry.Polygon([(0,0), (0, max_coord), (max_coord, max_coord), (max_coord, 0)])
uncovered_area = target_search_area.difference(poly)

x_coord = uncovered_area.centroid.coords.xy[0][0]
y_coord = uncovered_area.centroid.coords.xy[1][0]
print(int((x_coord) * 4000000 + y_coord))


### Version 1 of part 2 - doesnt finish bc space is too large

#grid = {i: set() for i in range(0, max_coord +1)}

#for line in input:
#    md = manhattan_distance(line[0:2], line[2:])
    # grid.update({(line[1]+i): grid[(line[1]+i)].union(range(((line[0] - (md-i)) if ((line[0] - (md-i)) > 0) else 0), \
    #                                                         ((line[0] + (md-i)) + 1 if ((line[0] + (md-i)) <= max_coord) else (max_coord + 1) ))) \
    #     for i in range(0, md) if ((line[1]+i) in grid.keys())})
    
    # grid.update({(line[1]-i): grid[(line[1]-i)].union(range(((line[0] - (md-i)) if ((line[0] - (md-i)) > 0) else 0), \
    #                                                         ((line[0] + (md-i)) + 1 if ((line[0] + (md-i)) <= max_coord) else (max_coord + 1) ))) \
    #     for i in range(0, md) if ((line[1]-i) in grid.keys())})
    # grid = {key: value for key, value in grid.items() if len(value) < max_coord + 1}


# y_coord = [key for key, values in grid.items() if len(values) < max_coord + 1]
# x_coord = set(range(0,max_coord)) - set(grid[y_coord[0]])

# (list(x_coord)[0]) * 4000000 + y_coord[0]