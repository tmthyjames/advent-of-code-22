# Day one

### Part one

with open('inputs/dayone.txt') as f:
    calorie_input = f.read().split('\n\n')

elves = []
for calories in calorie_input:
    elves.append(sum([int(calorie) for calorie in calories.split('\n')]))

print(max(elves))

#### Part two

sum(sorted(elves, reverse=True)[:3])