import string
lines = [str.strip(l, "\n") for l in open("input_day3.txt","r").readlines()]

compartments = [[list(rucksack[0:int(len(rucksack)/2)]), 
list(rucksack[int(len(rucksack)/2):])] for rucksack in lines]

comp1 = compartments[0][0]
comp2 = compartments[0][1]
common_values = [list(set(comp1).intersection(comp2)) for comp1, comp2 in compartments]
prio = dict(zip(string.ascii_lowercase[:26] + string.ascii_uppercase[:26], range(1,53)))
translate = [prio[v[0]] for v in common_values]
print(sum(translate))

# part 2
groups = [lines[i:i+3] for i in range(0, len(lines))[::3]]
badges = [list(set(e1).intersection(e2).intersection(e3)) for e1,e2,e3 in groups]
translate = [prio[v[0]] for v in badges]
print(sum(translate))