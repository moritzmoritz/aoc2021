import functools
import numpy as np

def solver_first(numbers_drawn, boards):
    for idx, number in enumerate(numbers_drawn):
        numbers_set = numbers_drawn[0:idx+1]

        # check each row if it has all
        for board in boards:
            board_won = False
            for row_idx in range(0,5):
                row = board[row_idx]
                
                match_count = functools.reduce(lambda r, x: r + 1 if x in numbers_set else r, row, 0)

                if match_count == 5:
                    board_won = True
                    break
        
            if not board_won:
                for column_idx in range(0,5):
                    column = board[:, column_idx]
                    
                    match_count = functools.reduce(lambda r, x: r + 1 if x in numbers_set else r, column, 0)

                    if match_count == 5:
                        board_won = True
                        break
            
            if board_won:
                all_numbers = board.flatten()
                unmarked_numbers = list(filter(lambda x: False if int(x) in numbers_set else True, all_numbers))
                sum = np.sum(unmarked_numbers)

                return sum * numbers_set[len(numbers_set) - 1]

def second_solver(numbers_drawn, boards):
    boards_won = []
    last_won_numbers_set = []
    for idx, number in enumerate(numbers_drawn):
        numbers_set = numbers_drawn[0:idx+1]

        # check each row if it has all
        for board_idx, board in enumerate(boards):
            board_won = False
            for row_idx in range(0,5):
                row = board[row_idx]
                
                match_count = functools.reduce(lambda r, x: r + 1 if x in numbers_set else r, row, 0)

                if match_count == 5:
                    board_won = True
                    break
        
            if not board_won:
                for column_idx in range(0,5):
                    column = board[:, column_idx]
                    
                    match_count = functools.reduce(lambda r, x: r + 1 if x in numbers_set else r, column, 0)

                    if match_count == 5:
                        board_won = True
                        break
            
            if board_won:
                if not board_idx in boards_won:
                    boards_won.append(board_idx)
                    last_won_numbers_set = numbers_set

    last_board_won = boards[boards_won[len(boards_won) - 1]]
    all_numbers = last_board_won.flatten()
    unmarked_numbers = list(filter(lambda x: False if int(x) in last_won_numbers_set else True, all_numbers))
    sum = np.sum(unmarked_numbers)

    return sum * last_won_numbers_set[len(last_won_numbers_set) - 1]

if __name__ == '__main__':
    lines = open('./input.txt', 'r').read().strip().split("\n")

    # First line is the input
    numbers_drawn = list(map(lambda x: int(x), lines[0].split(',')))
    
    boards = []
    current_board = np.zeros((5, 5))
    row_idx = 0

    for idx, line in enumerate(lines):
        if idx == 0:
            continue
        
        if row_idx == 5:
            boards.append(current_board)
            current_board = np.zeros((5, 5))
            row_idx = 0
        
        numbers = line.replace('  ', ' ').strip().split(' ')

        if len(numbers) == 5:
            for n_index, number in enumerate(numbers):
                current_board[row_idx][n_index] = int(number)
            
            row_idx += 1

        if idx == len(lines) - 1:
            boards.append(current_board)

    first_result = solver_first(numbers_drawn, boards)
    second_result = second_solver(numbers_drawn, boards)

    print(first_result, second_result)