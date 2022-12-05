# Part 1
lines = [str.strip(l, "\n") for l in open("input_day4.txt","r").readlines()]

pairs = [str.split(line, ",") for line in lines]
min_max_pairs = [[str.split(e1, "-"), str.split(e2, "-")] for e1, e2 in pairs]

# both smaller AND larger?
def does_a_contain_b(a, b):
    return (True if ((int(a[0]) <= int(b[0])) & (int(a[1]) >= int(b[1]))) else False)

print(sum([does_a_contain_b(e1, e2) | does_a_contain_b(e2, e1) for e1, e2 in min_max_pairs]))

# Part 2
def does_a_overlap_with_b(a, b):
    return (True if (int(a[1]) >= int(b[0])) & (int(b[0]) >= int(a[0])) else False)

print(sum([does_a_overlap_with_b(e1, e2) | does_a_overlap_with_b(e2, e1) for e1, e2 in min_max_pairs])
)