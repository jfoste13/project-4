import random, time, math

def puzzle_to_grid(puzzle):
    grid = []
    for i in range(10):
        grid.append(puzzle[i*10:((i+1)*10)])
    return(grid)
def display_puzzle(puzzle):
    print('Puzzle:\n')
    for row in puzzle:
        for cell in row:
            print('%s' % cell, end='')
        print()
    print()
def find_indexes(loc, word):
    ilist = []
    i = -1
    while True:
        i = loc.find(word, i + 1)
        if i == -1:
            break
        ilist.append(i)
    return ilist

def check_forward_row(puzzle, word):
    # solutions holds [row, column] solutions
    solutions = []
    for row in puzzle:
        solution_indexes = find_indexes(row, word)
        for si in solution_indexes:
            solutions.append([puzzle.index(row), si, '(FORWARD)'])
    return solutions
def check_backward_row(puzzle, word):
    new_puzzle = reverse(puzzle)
    solutions = []
    for row in new_puzzle:
        solution_indexes = find_indexes(row, word)
        for si in solution_indexes:
            solutions.append([new_puzzle.index(row), 9 - si, '(BACKWARD)'])
    return solutions

def check_forward_col(puzzle, word):
    new_puzzle = rotate_ccw(puzzle)
    solutions = []
    for row in new_puzzle:
        solution_indexes = find_indexes(row, word)
        for si in solution_indexes:
            solutions.append([row.index(word), 9 - new_puzzle.index(row), '(DOWN)'])
    return solutions
def check_backward_col(puzzle, word):
    new_puzzle = reverse(rotate_ccw(puzzle))
    solutions = []
    for row in new_puzzle:
        solution_indexes = find_indexes(row, word)
        for si in solution_indexes:
            solutions.append([9 - row.index(word), 9 - new_puzzle.index(row), '(UP)'])
    return solutions
def check_diagonal(puzzle, word):
    new_puzzle = diamond_45(puzzle)
    solutions = []
    for row in new_puzzle:
        solution_indexes = find_indexes(row, word)
        for si in solution_indexes:
            display_row = 0
            display_col = 0
            if new_puzzle.index(row) < 9:
                display_col = 9 - new_puzzle.index(row)
                display_row = row.index(word)
                solutions.append([display_row, display_col, '(DIAGONAL)'])
            elif new_puzzle.index(row) == 9:
                display_col = row.index(word)
                display_row = row.index(word)
                solutions.append([display_row, display_col, '(DIAGONAL)'])
            elif new_puzzle.index(row) > 9:
                display_col = row.index(word)
                display_row = 9 - (len(row) - row.index(word) - 1)
                solutions.append([display_row, display_col, '(DIAGONAL)'])
    return solutions


def reverse(puzzle):
    rev_row_grid = []
    for row in puzzle:
        rev_row_grid.append(''.join([row[9 - i] for i in range(10)]))
    return rev_row_grid

def rotate_ccw(puzzle):
    rotate_grid = []
    for i in range(10):
        piece = []
        for row in puzzle:
            piece.append(row[i])
        rotate_grid.append(''.join(piece))
    return [rotate_grid[len(rotate_grid) - i - 1] for i in range(len(rotate_grid))]

# note grid in [y][x] format
def diamond_45(puzzle):
    rotate_grid = [[] for i in range(19)]
    for i in range(10):
        y = 0
        x = 9 - i
        while not x == 10:
            rotate_grid[i].append(puzzle[y][x])
            x += 1
            y += 1
    for i in range(10):
        y = 1 + i
        x = 0
        while not y == 10:
            rotate_grid[i+10].append(puzzle[y][x])
            x += 1
            y += 1
    return [''.join(row) for row in rotate_grid]
