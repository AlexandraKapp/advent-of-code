import numpy as np# Part 1

input = [list(str.strip(l, "\n")) for l in open("input_day8.txt","r").readlines()]
lines = []
for row in input:
    lines.append([int(item) for item in row ])

columns = np.matrix(lines).T.tolist()

visible_from_left = []
visible_from_right = []
visible_from_top = []
visible_from_bottom = []
for row in lines:
    visible_from_left += [[True]+[row[i] > max(row[0:i]) for i in range(1, len(row))]]
    visible_from_right += [[row[i] > max(row[i+1:len(row)+1]) for i in range(0, len(row)-1)] + [True]]

for column in columns:
    visible_from_top += [[True]+[column[i] > max(column[0:i]) for i in range(1, len(column))]]
    visible_from_bottom += [[column[i] > max(column[i+1:len(column)+1]) for i in range(0, len(column)-1)] + [True]]

print((   np.matrix(visible_from_right) | 
    np.matrix(visible_from_left) | 
    np.matrix(visible_from_top).T | 
    np.matrix(visible_from_bottom).T
).sum())

# Part 2:
visible_to_left = []
visible_to_right = []
visible_to_top = []
visible_to_bottom = []

def visible_trees(tree_height, sub_row):
    greater_equal = [tree >= tree_height for tree in sub_row]
    if (True not in greater_equal):
        return len(sub_row)
    return (greater_equal.index(True) + 1)

for row in lines:
    visible_to_left += [[visible_trees(row[i], row[0:i][::-1]) for i in range(0, len(row))]]
    visible_to_right += [[visible_trees(row[i], row[i+1:len(row)]) for i in range(0, len(row))]]

for column in columns:
    visible_to_top += [[visible_trees(column[i], column[0:i][::-1]) for i in range(0, len(column))]]
    visible_to_bottom += [[visible_trees(column[i], column[i+1:len(column)]) for i in range(0, len(column))]]


scores = np.multiply(np.multiply(
    np.multiply( np.matrix(visible_to_left),
            np.matrix(visible_to_right)),
            np.matrix(visible_to_top).T),
            np.matrix(visible_to_bottom).T)
print(scores.max())