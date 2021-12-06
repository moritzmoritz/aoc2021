import numpy as np
import functools

def solver_first(points):
    # Find maximum x and y values
    max_x = functools.reduce(lambda r, x: x[0] if x[0] > r else r, points, 0)
    max_y = functools.reduce(lambda r, x: x[1] if x[1] > r else r, points, 0)
    
    field = np.zeros((max_x + 1, max_y + 1))
    
    for point in points:
        field[point[0], point[1]] += 1
    
    counts = field.flatten()
    filtered_counts = list(filter(lambda x: x >= 2, counts))
    return len(filtered_counts)

def solver_second(points):
    max_x = functools.reduce(lambda r, x: x[0] if x[0] > r else r, points, 0)
    max_y = functools.reduce(lambda r, x: x[1] if x[1] > r else r, points, 0)
    
    field = np.zeros((max_x + 1, max_y + 1))
    
    for point in points:
        field[point[0], point[1]] += 1
    
    counts = field.flatten()
    filtered_counts = list(filter(lambda x: x >= 2, counts))
    return len(filtered_counts)

def getEquidistantPoints(p1, p2, parts):
    return zip(np.linspace(p1[0], p2[0], parts+1),
               np.linspace(p1[1], p2[1], parts+1))

if __name__ == '__main__':
    lines = open('./input.txt', 'r').read().strip().split("\n")

    first_input_points = []
    second_input_points = []

    for line in lines:
        splitted_line = line.split(' -> ')
        start_point_input = splitted_line[0].split(',')
        start_point_input[0] = int(start_point_input[0])
        start_point_input[1] = int(start_point_input[1])
        
        end_point_input = splitted_line[1].split(',')
        end_point_input[0] = int(end_point_input[0])
        end_point_input[1] = int(end_point_input[1])

        if start_point_input[0] == end_point_input[0]:
            min_y = min(start_point_input[1], end_point_input[1])
            max_y = max(start_point_input[1], end_point_input[1])
            
            for y in range(min_y, max_y + 1):
                first_input_points.append([start_point_input[0], y])
                second_input_points.append([start_point_input[0], y])

        elif start_point_input[1] == end_point_input[1]:
            min_x = min(start_point_input[0], end_point_input[0])
            max_x = max(start_point_input[0], end_point_input[0])

            for x in range(min_x , max_x + 1):
                first_input_points.append([x, start_point_input[1]])
                second_input_points.append([x, start_point_input[1]])
        else:
            min_x = min(start_point_input[0], end_point_input[0])
            max_x = max(start_point_input[0], end_point_input[0])

            min_y = min(start_point_input[1], end_point_input[1])
            max_y = max(start_point_input[1], end_point_input[1])
            
            m = min(min_x, min_y)
            ma = max(max_x, max_y)
            
            points = np.linspace((min_x, min_y), (max_x, max_y), abs(max_y - min_x))
            print(points)
            break
            # for x in range(min_x, max_x + 1):
            #     for y in range(min_y, max_y + 1):
            #         # second_input_points.append([x, y])
            #         points = getEquidistantPoints


    first_result = solver_first(first_input_points)
    second_result = solver_second(second_input_points)

    print(first_result, second_result)