# Day six

with open('./inputs/daysix.txt', 'r') as f:
    buffer = f.read()

def detect_start(seq_length):
    counter = 0
    tracker = []
    for n, c in enumerate(buffer):
        tracker.append(c)
        if n >= (seq_length - 1):
            _tracker = tracker[counter:counter + seq_length]
            if len(_tracker) == len(set(_tracker)):
                return counter + seq_length
            counter += 1

### part one
print(detect_start(4))

### part two
print(detect_start(14))
