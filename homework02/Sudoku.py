from typing import Tuple, List, Set, Optional


def group(List: str, n: int):
    # Сгруппировать значения values в список, из списков по n элементов
    # >>> group([1,2,3,4], 2)
    # [[1, 2], [3, 4]]
    # >>> group([1,2,3,4,5,6,7,8,9], 3)
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a = []
    a = [List[:n]]
    for i in range(1, n):
        a = a + [List[i*n:n+n*i]]
    grid = a
    return grid


def read_sudoku(filename):
    with open(filename) as f:
        content = f.read()
    digits = [c for c in content if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(grid):
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(grid[row][col].center(width) + ('|' if str(
            col) in '25' else '') for col in range(9)))
    if str(row) in '25':
            print(line)
    print()


def get_row(values, pos):
    # Возвращает все значения для номера строки, указанной в pos
    # >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    # ['1', '2', '.']
    # >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    # ['4', '.', '6']
    # >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    # ['.', '8', '9']
    row, col = pos
    i = 0
    list = []
    for j in values:
        if i == row:
            list = j
        i += 1
    return list
    row, _ = pos
    return values[row]


def get_col(values, pos):
    # Возвращает все значения для номера столбца, указанного в pos
    # >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    # ['1', '4', '7']
    # >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    # ['2', '.', '8']
    # >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    # ['3', '6', '9']
    row, col = pos
    list = []
    for j in values:
        for i in range(len(j)):
            if i == col:
                list.append(j[i])
    return list


def get_block(values, pos):
    # Возвращает все значения из квадрата, в который попадает позиция pos
    # >>> grid = read_sudoku('puzzle1.txt')
    # >>> get_block(grid, (0, 1))
    # ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    # >>> get_block(grid, (4, 7))
    # ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    # >>> get_block(grid, (8, 8))
    # ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    row, col = pos
    i = 0
    j = 0
    list = []
    borderRow1 = 0
    borderRow2 = 0
    borderCol1 = 0
    borderCol2 = 0
    if (row <= 2) and (row >= 0):
        borderRow1 = 0
        borderRow2 = 2
    elif (row <= 5) and (row >= 3):
        borderRow1 = 3
        borderRow2 = 5
    else:
        borderRow1 = 6
        borderRow2 = 8
    if (col <= 2) and (col >= 0):
        borderCol1 = 0
        borderCol2 = 2
    elif (col <= 5) and (col >= 3):
        borderCol1 = 3
        borderCol2 = 5
    else:
        borderCol1 = 6
        borderCol2 = 8
    while i <= 8:
        while j <= 8:
            if ((i >= borderRow1) and (i <= borderRow2) and (
                    j >= borderCol1) and (j <= borderCol2)):
                list.append(values[i][j])
            j += 1
        j = 0
        i += 1
    return list


def find_empty_positions(grid: List[List[str]]) -> Optional[Tuple[int, int]]:
    # Найти первую свободную позицию в пазле
    # >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'],
    # ['7', '8', '9']]) (0, 2)
    # >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'],
    # ['7', '8', '9']]) (1, 1)
    # >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'],
    # ['.', '8', '9']]) (2, 0)
    row = 0
    missed_positions = []
    for i in grid:
        col = 0
        for j in i:
            if j == '.':
                missed_positions.append([row, col])
            col += 1
        row += 1
    missed = (missed_positions[0][0], missed_positions[0][1])
    return missed


def find_possible_values(grid, pos):
    # Вернуть множество возможных значения для указанной позиции
    # >>> grid = read_sudoku('puzzle1.txt')
    # >>> values = find_possible_values(grid, (0,2))
    # >>> values == {'1', '2', '4'}
    # True
    # >>> values = find_possible_values(grid, (4,7))
    # >>> values == {'2', '5', '9'}
    # True
    answer = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    list1 = get_row(grid, pos)
    for i in list1:
        for j in answer:
            if i == j:
                answer.remove(j)
    list2 = get_col(grid, pos)
    for i in list2:
        for j in answer:
            if i == j:
                answer.remove(j)
    list3 = get_block(grid, pos)
    for i in list3:
        for j in answer:
            if i == j:
                answer.remove(j)
    return answer


def solve(grid):
    # """ Решение пазла, заданного в grid """
    # """ Как решать Судоку?
    #     1. Найти свободную позицию
    #     2. Найти все возможные значения,
    # которые могут находиться на этой позиции
    #     3. Для каждого возможного значения:
    #         3.1. Поместить это значение на эту позицию
    #         3.2. Продолжить решать оставшуюся часть пазла
    # >>> grid = read_sudoku('puzzle1.txt')
    # >>> solve(grid)
    # [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    # ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    # ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    # ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    # ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    # ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    # ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    # ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    # ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    try:
        missed_position = find_empty_positions(grid)
    except IndexError:
        return grid

    possible_values = find_possible_values(grid, missed_position)
    for i in possible_values:
        grid[missed_position[0]][missed_position[1]] = i
        maybe = solve(grid)
        if maybe:
            return maybe

    grid[missed_position[0]][missed_position[1]] = '.'
    return None


def check_solution(solution):
    # Если решение solution верно, то вернуть True, в противном случае False
    # >>> a = [['4', '3', '4', '6', '7', '8', '9', '1', '2'],
    # ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    # ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    # ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    # ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    # ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    # ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    # ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    # ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    # >>> check_solution(a)
    # False
    # >>> grid = read_sudoku('puzzle1.txt')
    # >>> solution = solve(grid)
    # >>> check_solution(solution)
    # True
    list1 = [0]*9
    t = True
    for i in solution:
        if t:
            for j in i:
                if j == '.':
                    t = False
                    break
                else:
                    list1[int(j) - 1] += 1
                    if list1[int(j)-1] > 9:
                        t = False
                        break
        else:
            break
    if t:
        return True
    else:
        return False


def generate_sudoku(N):
    # Генерация судоку заполненного на N элементов
    # >>> grid = generate_sudoku(40)
    # >>> sum(1 for row in grid for e in row if e == '.')
    # 41
    # >>> solution = solve(grid)
    # >>> check_solution(solution)
    # True
    # >>> grid = generate_sudoku(1000)
    # >>> sum(1 for row in grid for e in row if e == '.')
    # 0
    # >>> solution = solve(grid)
    # >>> check_solution(solution)
    # True
    # >>> grid = generate_sudoku(0)
    # >>> sum(1 for row in grid for e in row if e == '.')
    # 81
    # >>> solution = solve(grid)
    # >>> check_solution(solution)
    # True
    grid = solve([['.'] * 9 for _ in range(9)])
    N = 81 - min(81, max(0, N))
    while N:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != '.':
            grid[row][col] = '.'
            N -= 1
    return grid


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)
