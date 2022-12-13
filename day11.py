from itertools import groupby
import numpy as np

# Part 1
input = [str.strip(l, "\n") for l in open("input_day11.txt","r").readlines()]
monkeys_input = [list(g) for k, g in groupby(input, key = bool) if k ]

class monkey:
    def __init__(self, monkey):
        self.inspection_counter = 0
        items = str.split(monkey[1], "  Starting items: ")[1]
        items = str.split(items, ", ")
        self.items = [int(item) for item in items]
        operation = str.split(monkey[2], "  Operation: new = old ")[1]
        operator = operation[0]
        if operation[2:] == "old":
            if operator == "*":
                self.operation = lambda x: x * x
            elif operator =="+":
                self.operation = lambda x: x+x
        else:
            number = int (operation[2:])
            if operator == "*":
                self.operation = lambda x: x * number
            elif operator =="+":
                self.operation = lambda x: x+ number
        self.divisor = int(str.split(monkey[3], "  Test: divisible by ")[1])
        self.test = lambda x: (x % self.divisor == 0)
        self.test_outcome_true = int(str.split(monkey[4], "    If true: throw to monkey ")[1])
        self.test_outcome_false = int(str.split(monkey[5], "    If false: throw to monkey ")[1])


monkeys = {i: monkey(monkeys_input[i]) for i in range(0, len(monkeys_input))}

for round in range(0, 20):
    for i in range(0, len(monkeys)):
        for item in monkeys[i].items:
            monkeys[i].inspection_counter += 1
            # operation
            worry_level = int(monkeys[i].operation(item) / 3)
            if monkeys[i].test(worry_level):
                monkeys[monkeys[i].test_outcome_true].items += [worry_level]
            else:
                monkeys[monkeys[i].test_outcome_false].items += [worry_level]

        # reset items
        monkeys[i].items = []
    

#for key, value in monkeys.items():
#    print(f"{key}: {value.inspection_counter}")

inspection_values = [value.inspection_counter for value in monkeys.values()]
inspection_values.sort()
print(inspection_values[-2] * inspection_values[-1])


divisor = [m.divisor for m in monkeys.values()]
greatest_common_divisor = np.prod(divisor)


# Part 2:
monkeys = {i: monkey(monkeys_input[i]) for i in range(0, len(monkeys_input))}

for round in range(0, 10000):
    for i in range(0, len(monkeys)):
        for item in monkeys[i].items:
            monkeys[i].inspection_counter += 1
            # operation
            worry_level = int(monkeys[i].operation(item)) % greatest_common_divisor
            if monkeys[i].test(worry_level):
                monkeys[monkeys[i].test_outcome_true].items += [worry_level]
            else:
                monkeys[monkeys[i].test_outcome_false].items += [worry_level]

        # reset items
        monkeys[i].items = []
    

inspection_values = [value.inspection_counter for value in monkeys.values()]
inspection_values.sort()
print(inspection_values[-2] * inspection_values[-1])