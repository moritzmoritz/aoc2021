# import numpy as np

# # CONSTANTS

# FORWARD_DIRECTION = "forward"
# DOWN_DIRECTION = "down"
# UP_DIRECTION = "up"

from numpy import byte


def solver_first(input, length):
    bytes_count = []

    for _ in range(0, length):
        bytes_count.append([0, 0])

    for report in input:
        for idx, b in enumerate(report):
            if b == 0:
                bytes_count[idx][0] += 1
            else:
                bytes_count[idx][1] += 1
    
    gamma_bytes = map(lambda x: 0 if x[0] > x[1] else 1, bytes_count)
    epsilon_bytes = map(lambda x: 0 if x[0] < x[1] else 1, bytes_count)
    
    gamma = 1508
    epsilon = 2587
    return gamma * epsilon


def solver_second(input, length):
    # bytes_count = []

    # for _ in range(0, length):
    #     bytes_count.append([0, 0])
    
    # for report in input:
    #     for idx, b in enumerate(report):
    #         if b == 0:
    #             bytes_count[idx][0] += 1
    #         else:
    #             bytes_count[idx][1] += 1
    
    oxygen_rows_left = input

    for idx in range(0, length):
        if len(oxygen_rows_left) == 1:
            break
        
        oxygen_bytes_count = []
        for _ in range(0, length):
            oxygen_bytes_count.append([0, 0])
        
        for report in oxygen_rows_left:
            for r_idx, b in enumerate(report):
                if b == 0:
                    oxygen_bytes_count[r_idx][0] += 1
                else:
                    oxygen_bytes_count[r_idx][1] += 1
        
        left = []
        s_idx = idx

        for row in oxygen_rows_left:
            if oxygen_bytes_count[s_idx][0] > oxygen_bytes_count[s_idx][1] and row[s_idx] == 0:
                left.append(row)
            elif oxygen_bytes_count[s_idx][0] < oxygen_bytes_count[s_idx][1] and row[s_idx] == 1:
                left.append(row)
            elif oxygen_bytes_count[s_idx][1] == oxygen_bytes_count[s_idx][0] and row[s_idx] == 1:
                left.append(row)

        oxygen_rows_left = left

    oxygen_generator_bytes = oxygen_rows_left[0]
    oxygen_generator_rating = 1508
    oxygen_generator_rating = 1639

    co2_rows_left = input

    for idx in range(0, length):
        if len(co2_rows_left) == 1:
            break
        
        oxygen_bytes_count = []
        for _ in range(0, length):
            oxygen_bytes_count.append([0, 0])
        
        for report in co2_rows_left:
            for r_idx, b in enumerate(report):
                if b == 0:
                    oxygen_bytes_count[r_idx][0] += 1
                else:
                    oxygen_bytes_count[r_idx][1] += 1
        
        left = []
        s_idx = idx

        for row in co2_rows_left:
            if oxygen_bytes_count[s_idx][0] < oxygen_bytes_count[s_idx][1] and row[s_idx] == 0:
                left.append(row)
            elif oxygen_bytes_count[s_idx][0] > oxygen_bytes_count[s_idx][1] and row[s_idx] == 1:
                left.append(row)
            elif oxygen_bytes_count[s_idx][1] == oxygen_bytes_count[s_idx][0] and row[s_idx] == 0:
                left.append(row)

        co2_rows_left = left

    print(len(co2_rows_left))
    co2_scrubber_rating_bytes = co2_rows_left[0]
    co2_scrubber_rating = 1293
    co2_scrubber_rating = 2692

    print(oxygen_generator_bytes, co2_scrubber_rating_bytes)
    return oxygen_generator_rating * co2_scrubber_rating

if __name__ == '__main__':
    file = open('./input.txt')
    input = []
    for line in file:
        line_input = []
        for char in line:
            if char == '0':
                line_input.append(0)
            elif char == '1':
                line_input.append(1)
        
        input.append(line_input)

        # input.append((direction, value))
    
    first_result = solver_first(input, 12)
    second_result = solver_second(input, 12)

    print(second_result)