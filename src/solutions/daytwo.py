# Day two

### part one

with open('inputs/daytwo.txt') as f:
    moves = f.read().split('\n')
    round_inputs = [move.split() for move in moves]


def calculate_points(their_move, your_move):
    their_move_points = point_mapper[their_move]
    your_move_points = point_mapper[your_move]

    action = [their_move, your_move]

    if their_move == your_move:
        their_result = your_result = 'draw'
    elif action in your_winning_actions:
        your_result, their_result = 'win', 'lose'
    elif action not in your_winning_actions:
        their_result, your_result = 'win', 'lose'

    their_round_points = point_mapper[their_result]
    your_round_points = point_mapper[your_result]

    return (their_move_points + their_round_points, your_move_points + your_round_points)


point_mapper = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    'lose': 0,
    'win': 6,
    'draw': 3
}

move_mapper = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

your_winning_actions = [
    ['rock', 'paper'],
    ['paper', 'scissors'],
    ['scissors', 'rock']
]

their_total_points = 0
your_total_points = 0

for round_ in round_inputs:
    their_move = move_mapper[round_[0]]
    your_move = move_mapper[round_[1]]

    their_round_points, your_round_points = calculate_points(their_move, your_move)

    your_total_points += your_round_points
    their_total_points += their_round_points

print(your_total_points)

### part two

round_decider = {
    'scissors': {
        'X': 'paper',
        'Y': 'scissors',
        'Z': 'rock'
    },
    'rock': {
        'X': 'scissors',
        'Y': 'rock',
        'Z': 'paper'
    },
    'paper': {
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors'
    }
}

their_total_points = 0
your_total_points = 0
for round_ in round_inputs:
    their_move = move_mapper[round_[0]]
    your_move = round_decider[move_mapper[round_[0]]][round_[1]]

    their_round_points, your_round_points = calculate_points(their_move, your_move)

    your_total_points += your_round_points
    their_total_points += their_round_points

print(your_total_points)