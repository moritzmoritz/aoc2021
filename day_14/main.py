from collections import Counter

def solver(template, freqs, transitions, steps):
    character_counts = Counter(template)

    for _ in range(steps):
        tmp = Counter()

        for pair, count in freqs.items():
            if pair in transitions:
                character_counts[transitions[pair][0][1]] += count

                for new_pair in transitions[pair]:
                    tmp[new_pair] += count
            
            freqs = tmp

    common_characters = character_counts.most_common()

    return common_characters[0][1] - common_characters[-1][1]

if __name__ == '__main__':
    lines = open('input.txt','r').read().split('\n')
    
    template = ''
    freqs = Counter()
    transitions = {}

    for line in lines:
        if len(line) == 0:
            continue
            
        if ' -> ' in line:
            x, y = line.split(" -> ")
            transitions[x] = [x[0]+y, y+x[1]]
        else:
            template = line

    for l, r in zip(template, template[1:]):
        s = l + r
        freqs[s] += 1

    first_result = solver(template, freqs, transitions, 10)
    second_result = solver(template, freqs, transitions, 40)
    print(first_result, second_result)