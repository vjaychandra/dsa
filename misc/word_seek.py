
def form_word_directions(input_str):

    length = input_str.index('\n')+1
    characters = [(letter, divmod(index, length))
                for  index, letter in enumerate (input_str)]

    word_grid = {}
    directions = {'down':0, 'down and left diagonally':-1, 'down and right diagonally':1}

    for word_direction, directions in directions.items():
        word_grid[word_direction] = []
        for x in range(length):
            for i in range(x, len(characters), length + directions):
                word_grid[word_direction].append(characters[i])
            word_grid[word_direction].append('\n')

    word_grid['going right'] = characters
    word_grid['going left'] = [i for i in reversed(characters)]
    word_grid['up'] = [i for i in reversed(word_grid['down'])]
    word_grid['up and left diagonally'] = [i for i in reversed(word_grid['down and right diagonally'])]
    word_grid['up and right diagonally'] = [i for i in reversed(word_grid['down and left diagonally'])]

    return word_grid


def find_words(lines, op_words):

    op_dict = {}
    direction = "down"
    
    for direction, line_data in lines.items():
        string = ''.join([i[0] for i in line_data])
        for word in op_words:
            if word in string:
                p1, p2 = line_data[string.index(word)][1]
                op_dict[word] = f"{word} {p1} {p2}"
    return op_dict


input_str ='''ELEKTRAHTHORGV
SILVERAORWTNSH
AUAUAWREHSINUP
HNERKCTNWHAMRR
AFTEHSIITMASFA
ICYMILDRRNCAEA
IEIMAOIEEAERRL
WWYTWNDVRMGEIO
INVIDIBLEGAGRO
TDHSPAEOHDCNOP
CIOSKTTZTGEAND
HFKOKPRNNLKRMA
EBWOMANPAEUTAE
UOFALCONPFLSND'''

solutions = ["ANTMAN","DAREDEVIL", "DEADPOOL","ELEKTRA","HAWKEYE","PUNISHER","THING","WITCH"]

word_grid = form_word_directions(input_str)
output = find_words(word_grid, solutions)

for word in solutions:
    if output.get(word):
        print(output[word])
    else:
        print(word, -1, -1)

