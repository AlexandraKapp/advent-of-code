# Part 1
input = [str.strip(l, "\n") for l in open("input_day10.txt","r").readlines()]
lines = [str.split(line, " ") for line in input]

cycle_no = 0
x = 1
cycle = {}
for command in lines:
    if command[0] == "noop":
        cycle_length = 1
    elif command[0] == "addx":
        cycle_length = 2
    
    for i in range(0,cycle_length):
        cycle_no += 1
        cycle[cycle_no] = cycle_no * x
        if i == 1:
            x += int(command[1])

print(cycle[20] + cycle[60] + cycle[100] + cycle[140] + cycle[180] + cycle[220])

# Part 2

output = []
cycle_no = 1
x = 1

for command in lines:
    if command[0] == "noop":
        cycle_length = 1
    elif command[0] == "addx":
        cycle_length = 2
    
    for i in range(0,cycle_length):
        current_crt = ((cycle_no) % 40)
        cycle_no += 1
        if current_crt in range(x, x+3):
            output += ["#"]
        else:
            output += ["."]
            
        if i == 1:
            x += int(command[1])

output_lines = [output[i:i+40] for i in range(0, len(output), 40)]
with open("day10_output.txt","w") as file:
    for line in output_lines:
        file.write("".join(line + ["\n"])) 