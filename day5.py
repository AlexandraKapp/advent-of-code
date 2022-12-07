# Part 1
lines = [str.strip(l, "\n") for l in open("input_day5.txt","r").readlines()]
stacks_raw = lines [0:lines.index("")-1]
movements = lines[lines.index("")+1:]

groups = [[str.replace(s[i:i+4], " ", "").strip("[]") for i in range(0, len(s))[::4]] for s in stacks_raw]
groups.reverse()

# using numpy
import numpy as np
stacks = np.matrix(groups).T.tolist()

# without numpy

# s1 = []
# s2 =[]
# s3 = []
# s4 = []
# s5 = []
# s6 = []
# s7 = []
# s8 = []
# s9 = []
# for g in groups:
#     s1 = s1 + [g[0]]
#     s2 = s2 + [g[1]]
#     s3 = s3 + [g[2]]
#     s4 = s4 + [g[3]]
#     s5 = s5 + [g[4]]
#     s6 = s6 + [g[5]]
#     s7 = s7 + [g[6]]
#     s8 = s8 + [g[7]]
#     s9 = s9 + [g[8]]

# # reverse order
# s1.reverse()
# s2.reverse()
# s3.reverse()
# s4.reverse()
# s5.reverse()
# s6.reverse()
# s7.reverse()
# s8.reverse()
# s9.reverse()

# # concatinate all stacks to a single list of lists
# stacks = [s1,s2,s3,s4,s5,s6,s7,s8,s9]

# remove empty elements
stacks = [[e for e in s if e != ''] for s in stacks]

def move(from_id, to_id, stack):
    stack[to_id] = stack[to_id] + [stack[from_id][-1]]
    stack[from_id].pop()
    return stack

def move_elements (movement, stack):
    for i in range(0, movement[0]):
        stack = move(movement[1]-1, movement[2]-1, stack)
    return(stack)

import copy
stacks1 = copy.deepcopy(stacks)
movements = [str.split(str.strip(move_string, "move "), " from ") for move_string in movements]
movements = [[int(how_many)] + list(map(int, str.split(from_to, " to "))) for how_many, from_to in movements]
for m in movements:
   stacks1 = move_elements(m, stacks1)

print("".join([e[-1] for e in stacks1]))

# Part 2:
def move_elements2 (movement, stack):
    how_many = movement[0]
    from_id = movement[1]-1
    to_id = movement[2]-1
    stack[to_id] = stack[to_id] + stack[from_id][len(stack[from_id])-how_many: len(stack[from_id])]
    stack[from_id] = stack[from_id][0:len(stack[from_id])-how_many]
    return(stack)

stacks2 = copy.deepcopy(stacks)
for m in movements:
   stacks2 = move_elements2(m, stacks2)

print("".join([e[-1] for e in stacks2]))