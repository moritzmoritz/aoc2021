def fuel_cost(crabs,current_crab_pos,step_cost):
    fuel = 0

    for other_crab_position in crabs:
        steps = abs(other_crab_position-current_crab_pos)
        fuel += steps if step_cost == 1 else steps * (steps + 1 ) / 2

    return fuel

def solver(crabs, cost):
    costs = []

    for crab in range(min(crabs), max(crabs)): 
        costs = costs + [fuel_cost(crabs,crab,cost)]
    
    return min(costs)

if __name__ == '__main__':
    crabs = list(map(int, open('input.txt','r').read().split(',')))
    
    first_result = solver(crabs, 1)
    second_result = solver(crabs, 2)

    print(first_result, second_result)