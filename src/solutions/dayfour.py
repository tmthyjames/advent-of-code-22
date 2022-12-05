# Day 4

### part one

with open('./inputs/dayfour.txt', 'r') as f:
    input_items = [i.split(',') for i in f.read().split('\n')]


def apply_conditionals(conditionals1, conditionals2, operator=all):
    if operator(conditionals1) or operator(conditionals2):
        return 1
    else:
        return 0


def main(input_items, operator="any"):
    counter = 0
    for n, assignments in enumerate(input_items):
        assignment1 = [int(i) for i in assignments[0].split('-')]
        assignment2 = [int(i) for i in assignments[1].split('-')]

        sections1 = list(range(assignment1[0], assignment1[1] + 1))

        sections2 = list(range(assignment2[0], assignment2[1] + 1))

        returned_counter = apply_conditionals(
            [sections2[0] in sections1, sections2[-1] in sections1],
            [sections1[0] in sections2, sections1[-1] in sections2],
            operator=operator
        )

        counter += returned_counter

    return counter


print(main(input_items, all))

# part two: change to OR
print(main(input_items, any))