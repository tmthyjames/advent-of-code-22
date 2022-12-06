# Day 5

### Part one

with open('./inputs/dayfive.txt', 'r') as f:
    stacks, moves_blob = f.read().split('\n\n')

blobs = list(reversed([i.replace('    ', '[ ]').replace(' ', '') for i in stacks.split('\n')]))

def get_stack_ids(blobs):
    stack_ids = {int(i): [] for i in blobs[0]}
    for blob in blobs[1:]:
        blocks = blob.split('][')
        for n,block in enumerate(blocks):
            key = n+1
            letter = block.replace('[', '').replace(']', '')
            if not letter.isalpha(): continue
            stack_ids[key].append(letter)
    return stack_ids


stack_ids = get_stack_ids(blobs)

moves = moves_blob.split('\n')

for move in moves:
    quantity, from_stack, to_stack = [int(m) for m in move.split(' ') if m.isdigit()]
    for crate in range(0, quantity):
        stack_ids[to_stack].append(stack_ids[from_stack].pop())

print(''.join([stack_ids[i][-1] for i in stack_ids.keys()]))

### part two

stack_ids = get_stack_ids(blobs)
moves = moves_blob.split('\n')

for move in moves:
    quantity, from_stack, to_stack = [int(m) for m in move.split(' ') if m.isdigit()]
    for crate in stack_ids[from_stack][-quantity:]:
        stack_ids[to_stack].append(crate)
    stack_ids[from_stack] = stack_ids[from_stack][0:-quantity:]

print(''.join([stack_ids[i][-1] for i in stack_ids.keys()]))
