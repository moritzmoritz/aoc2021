def solver(fishes, days):
    fishes_after_n_days = [1] * 9
    
    # Calculate number of fishes after n days in each level
    for i in range(0, days):
        fishes_after_n_days = [fishes_after_n_days[6] + fishes_after_n_days[8]] + fishes_after_n_days[:-1]

    # Sum them up
    sum = 0
    for i in range(0, 9):
        sum += fishes_after_n_days[i] * fishes[i]
    
    return sum

if __name__ == '__main__':
    fishes = open('input.txt','r').read().split(',')

    # Calculate inital fishes for each level
    input = [0] * 9
    for fish in fishes:
        input[int(fish)] += 1

    first_result = solver(input, 80)
    second_result = solver(input, 256) 

    print(first_result, second_result)