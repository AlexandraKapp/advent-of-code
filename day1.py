# Solution 1: (ugly)

#### part 1 #####

f = open("input_day1.txt","r")
lines = f.readlines()


current_elves_no = 1
current_elves_calories = 0

top1_elves_no = 0
top1_elves_calories = 0

for line in lines:
    if line == "\n":

        # update the max elve if the current elve carries more calories
        if current_elves_calories > top1_elves_calories:
            top1_elves_no = current_elves_no
            top1_elves_calories = current_elves_calories

        # move to next elve
        current_elves_no += 1
        current_elves_calories = 0
    else:
        calories = int(str.strip(line, "\n"))
        current_elves_calories += calories

print("Solution 1:")
print("Part 1")
print(f"No. of elve: {top1_elves_no}")
print(f"Calories: {top1_elves_calories}")



#### Part 2 #####

f = open("input_day1.txt","r")
lines = f.readlines()


current_elves_no = 1
current_elves_calories = 0

top1_elves_no = 0
top1_elves_calories = 0

top2_elves_no = 0
top2_elves_calories = 0

top3_elves_no = 0
top3_elves_calories = 0

for line in lines:
    if line == "\n":

        # update the max elve if the current elve carries more calories
        if current_elves_calories > top1_elves_calories:

            # move others down in the ranking:
            top3_elves_no = top2_elves_no
            top3_elves_calories = top2_elves_calories
            
            top2_elves_no = top1_elves_no
            top2_elves_calories = top1_elves_calories

            # assign new elve to top1
            top1_elves_no = current_elves_no
            top1_elves_calories = current_elves_calories

        elif current_elves_calories > top2_elves_calories:
            
            # move others down in the ranking:
            top3_elves_no = top2_elves_no
            top3_elves_calories = top2_elves_calories
            
            # assign new elve to top2
            top2_elves_no = current_elves_no
            top2_elves_calories = current_elves_calories

        elif current_elves_calories > top3_elves_calories:
            
            # assign new elve to top3
            top3_elves_no = current_elves_no
            top3_elves_calories = current_elves_calories

        # move to next elve
        current_elves_no += 1
        current_elves_calories = 0
    else:
        calories = int(str.strip(line, "\n"))
        current_elves_calories += calories

top3_calories_combined = top1_elves_calories + top2_elves_calories + top3_elves_calories

print("Part 2")
print(f"No. of elves: {top1_elves_no}, {top2_elves_no}, {top3_elves_no}")
print(f"Calories combined: {top3_calories_combined}")



### Solution 2 (pretty):

lines = open("input_day1.txt","r").readlines()

indices_breaks = [i for i in range(len(lines)) if lines[i] == "\n"]
lines = [str.strip(l, "\n") for l in lines]
list_of_elves = [lines[i+1: j] for i, j in zip([-1] + indices_breaks, indices_breaks +[len(lines)])]
calories = [sum(list(map(int, elves))) for elves in list_of_elves]

print("\nSolution 2:")
# Part 1:
print("Part 1")
print(f"Calories: {max(calories)}")

# Part 2:
print("Part 2")
calories.sort(reverse=True)
print(f"Calories combined: {sum(calories[0:3])}")
