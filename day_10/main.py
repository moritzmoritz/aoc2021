OPENING_CHARS = '([{<'
CLOSING_CHARS = ')]}>'
CHAR_ERROR_SCORES = {')':3,']':57,'}':1197,'>':25137}
CHAR_ERROR_SCORES_SECOND = {')':1,']':2,'}':3,'>':4}

def line_corrupted(line):
    closing_chars = []

    for idx in range(len(line)):
        if(line[idx] in OPENING_CHARS):
            closing_chars.append(CLOSING_CHARS[OPENING_CHARS.index(line[idx])])
        elif(closing_chars[-1] != line[idx]):
            # Corrupted line - add to score
            score = CHAR_ERROR_SCORES.get(line[idx])
            return score, True, []
        else:
            closing_chars = closing_chars[:-1]

    return 0, False, closing_chars

def solver_first(lines):
    score = 0
    for line in lines:
        line_score, corrupted, _ = line_corrupted(line)

        if corrupted:
            score += line_score

    return score

def solver_second(lines):
    scores = []
    for line in lines:
        closing_chars = []
        score = 0
        corrupted_line = False

        for idx in range(len(line)):
            _, corrupted, closing_chars = line_corrupted(line)

            if corrupted:
                corrupted_line = True

        if not corrupted_line:
            for idx in reversed(closing_chars):
                score = score * 5 + CHAR_ERROR_SCORES_SECOND.get(idx)
            scores.append(score)

    scores.sort()
    return scores[int(len(scores) / 2)]

if __name__ == '__main__':
    lines = open('input.txt','r').read().split('\n')
    
    first_result = solver_first(lines)
    second_result = solver_second(lines)

    print(first_result, second_result)

