# Part 1
lines = [str.strip(l, "\n") for l in open("input_day6.txt","r").readlines()]
unique_characters = [len(set(lines[0][i:i+4])) for i in range(0, len(lines[0]))]
print("Part 1:")
print(unique_characters.index(4) + 4)
# one liner
print("one liner:")
print([len(set(lines[0][i:i+4])) for i in range(0, len(lines[0]))].index(4) + 4)

# Part 2
unique_characters = [len(set(lines[0][i:i+14])) for i in range(0, len(lines[0]))]
print("Part 2:")
print(unique_characters.index(14) + 14)