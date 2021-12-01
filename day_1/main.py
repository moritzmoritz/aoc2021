import numpy as np
import functools
from os import initgroups


def solver_first(input):
    input_data = np.array(input)
    input_diff = np.diff(input_data)

    return functools.reduce(lambda x, y : x + 1 if y > 0 else x, input_diff, 0)

def solver_second(input):
    sliding_windows = np.lib.stride_tricks.sliding_window_view(input, 3)
    sums = [np.sum(a) for a in sliding_windows]
    sums_diff = np.diff(sums)
        
    return functools.reduce(lambda x, y : x + 1 if y > 0 else x, sums_diff, 0)

if __name__ == '__main__':
    file = open('./input.txt')
    input = []
    for line in file:
        input.append(int(line))
    
    first_result = solver_first(input)
    second_result = solver_second(input)
    
    print('first', first_result)
    print('second', second_result)