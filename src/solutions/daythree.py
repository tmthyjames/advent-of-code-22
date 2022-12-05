# Day three

### part one

with open('./inputs/daythree.txt', 'r') as f:
    input_items = f.read().split('\n')

points = {
    **{chr(i):n+1 for n,i in enumerate(range(ord('a'),ord('z')+1))},
    **{chr(i):n+27 for n,i in enumerate(range(ord('A'),ord('Z')+1))}
}

total_points = []
for n,item in enumerate(input_items):
    comp_one = item[:int(len(item)/2)]
    comp_two = item[int(len(item)/2):]
    overlap = set(comp_one).intersection(comp_two)
    if overlap:
        priority = overlap.pop()
        total_points.append(points[priority])

print(sum(total_points))

### part two

def chunks(xs, n):
    n = max(1, n)
    return (xs[i:i+n] for i in range(0, len(xs), n))

total_points = []
for groups in list(chunks(input_items, 3)):
    group_badge = set(groups[0]).intersection(set(groups[1])).intersection(groups[2])
    total_points.append(points[group_badge.pop()])
print(sum(total_points))