from itertools import groupby

input = [str.strip(l, "\n") for l in open("input_day13.txt","r").readlines()]
input = [(list(g)) for k, g in groupby(input, key=bool) if k]
input = [[eval(element[0]), eval(element[1])] for element in input]

def compare_elements(left, right):
    if left == right:
        return None
    elif left < right:
        return True
    elif left > right:
        return False

def compare_lines(left, right):
    if isinstance(left, list) |  isinstance(right, list):
        left = left if isinstance(left, list) else [left]
        right = right if isinstance(right, list) else [right]
        for i in range(0, len(left)):
            # right runs out
            if len(right) < i+1:
                return False
            result = compare_lines(left[i], right[i])
            if result is None:
                continue
            else:
                return result
                
        # left side ran out            
        if len(right) > len(left):
            return True
    else:
        return compare_elements(left, right)
    
print(sum([i+1 for i in range(0, len(input)) if compare_lines(input[i][0], input[i][1]) ]))

input = [line[0] for line in input] + [line[1] for line in input] 

def get_elements(elements):
    flattend = []
    if len(elements) == 0:
        return (flattend + [-1])
    for element in elements:
        if isinstance(element, list):
                flattend += get_elements(element)
        else:
            flattend += [element]
    return flattend

flattened = [get_elements(line) for line in input]
flattened += [[2]]
flattened += [[6]]

flattened.sort()

print((flattened.index([2])+1)  * (flattened.index([6])+1))