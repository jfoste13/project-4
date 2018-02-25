from funcs import *

def main():
    # parse input and display puzzle
    puzzle_info = input()
    puzzle = puzzle_to_grid(puzzle_info[0:100])
    words = puzzle_info[100:].split(' ')
    display_puzzle(puzzle)
    if not words == ['']:
        for word in words:
            solutions = check_forward_row(puzzle, word) + check_backward_row(puzzle, word) + check_forward_col(puzzle, word) + check_backward_col(puzzle, word) + check_diagonal(puzzle, word)
            if not solutions:
                print('%s: word not found' % word)
            else:
                for solution in solutions:
                    print('%s: %s row: %d column: %d' % (word, solution[2], solution[0], solution[1]))

if __name__ == '__main__':
    main()
