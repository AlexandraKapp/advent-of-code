lines = [str.strip(l, "\n") for l in open("input_day2.txt","r").readlines()]
lines = [str.split(element, " ") for element in lines]

def get_points(other, me): #(return: win?, what is it?)
    if other == "A":
        if me == "X":
            return (3, 1)
        elif me == "Y":
            return (6, 2)
        elif me == "Z":
            return (0, 3) 
    elif other == "B":
        if me == "X":
            return (0, 1)
        elif me == "Y":
            return (3, 2)
        elif me == "Z":
            return (6, 3) 
    elif other == "C":
        if me == "X":
            return (6, 1)
        elif me == "Y":
            return (0, 2)
        elif me == "Z":
            return (3, 3) 

print("Part 1:")
print(sum([sum(get_points(i, j)) for i, j in lines]))

def get_points2(other, me): #(return: win?, what is it?)
    if other == "A":# rock
        if me == "X": # loose: sissorrs
            return (0, 3)
        elif me == "Y":
            return (3, 1) # tie: rock
        elif me == "Z":
            return (6, 2) # win: paper
    elif other == "B": # paper
        if me == "X": # loose: rock
            return (0, 1)
        elif me == "Y": # tie: paper
            return (3, 2)
        elif me == "Z": # win: scissors
            return (6, 3) 
    elif other == "C": # scissors
        if me == "X":
            return (0, 2) # loose: paper
        elif me == "Y":
            return (3, 3) # tie: scissors
        elif me == "Z":
            return (6, 1) # win: rock

print("Part 2:")
print(sum([sum(get_points2(i, j)) for i, j in lines]))