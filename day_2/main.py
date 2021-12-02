import numpy as np

# CONSTANTS

FORWARD_DIRECTION = "forward"
DOWN_DIRECTION = "down"
UP_DIRECTION = "up"

def solver_first(input):
    filtered_horizontal_list = list(filter(lambda x: x[0] == FORWARD_DIRECTION, input))
    filtered_depth_list = list(filter(lambda x: x[0] != FORWARD_DIRECTION, input))
    
    horizontal = np.sum(list(map(lambda x: x[1], filtered_horizontal_list)))
    depth = np.sum(list(map(lambda x: x[1] if x[0] == DOWN_DIRECTION else -x[1], filtered_depth_list)))

    return horizontal * depth

def solver_second(input):
    horizontal = 0
    depth = 0
    aim = 0
    
    for movement in input:
        if movement[0] == FORWARD_DIRECTION:
            horizontal += movement[1]
            depth += aim * movement[1]
        elif movement[0] == DOWN_DIRECTION:
            aim += movement[1]
        elif movement[0] == UP_DIRECTION:
            aim -= movement[1]

    return horizontal * depth

if __name__ == '__main__':
    file = open('./input.txt')
    input = []
    for line in file:
        splitted_line = line.split(' ')
        direction = splitted_line[0]
        value = int(splitted_line[1])

        input.append((direction, value))
    
    first_result = solver_first(input)
    second_result = solver_second(input)
    print(first_result, second_result)