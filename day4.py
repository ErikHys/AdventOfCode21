import math

with open("inputs/input_day_4.txt") as file:
    numbers = [int(x) for x in file.readline().split(',')]
    boards_in = file.read().split('\n\n')


def create_board(board_in):
    return [[int(x) for x in line.split()] for line in board_in.split('\n') if len(line) > 1]


def check_boards(board, played_numbers):
    for i in range(5):
        for j in range(5):
            if board[i][j] not in played_numbers:
                break
            if j == 4:
                return True, board[i]
    for j in range(5):
        for i in range(5):
            if board[i][j] not in played_numbers:
                break
            if i == 4:
                return True, [board[i][z] for z in range(5)]
    return False, [0]


boards = [create_board(x) for x in boards_in]


def run():
    played_numbers = set()
    for n in numbers:
        played_numbers.add(n)
        for board in boards:
            complete, result = check_boards(board, played_numbers)
            if complete:
                print(result)
                print(sum([sum([x for x in line if x not in played_numbers]) for line in board]), n)
                print(sum([sum([x for x in line if x not in played_numbers]) for line in board])*n)
                return


run()

# part 2


def run_last():
    played_numbers = set()
    for n in numbers:
        played_numbers.add(n)
        for board in boards:
            complete, result = check_boards(board, played_numbers)
            if complete and len(boards) == 1:
                print(sum([sum([x for x in line if x not in played_numbers]) for line in boards[0]]), n)
                print(sum([sum([x for x in line if x not in played_numbers]) for line in boards[0]]) * n)
                return
            elif complete:
                boards.remove(board)


run_last()