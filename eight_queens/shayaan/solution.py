""" Solves the n queens problem """
__author__ = 'Shayaan Syed Ali'
__email__ = 'shayaan.syed.ali@gmail.com'


from utils import *


QUEEN = 'Q'
EMPTY = '.'


# region Solutions

def greedy_solution(n):
    """ Search for a solution and test it's viability greedily """

    positions = set_of_positions(n)

    def greedy_solution_recursive(remaining_positions, n_remaining_queens):
        """ Returns the positions of queens via a recursive, greedy, brute force approach """
        if n_remaining_queens == 1:
            for position in remaining_positions:
                yield [position]
        while remaining_positions:
            position = remaining_positions.pop()
            subsolution_remaining_positions = remaining_positions - threatened_positions(*position, n)
            for subsolution_positions in greedy_solution_recursive(
                    subsolution_remaining_positions, n_remaining_queens - 1):
                yield [position] + subsolution_positions

    def convert_queen_positions_to_a_board(queen_positions):
        board = [[EMPTY for _ in range(n)] for _ in range(n)]
        for i, j in queen_positions:
            board[i][j] = QUEEN
        return board

    solutions = greedy_solution_recursive(positions, n)
    return (convert_queen_positions_to_a_board(solution) for solution in solutions)


# These are the keywords to select each algorithm in the parser
solution_functions = {
    'greedy': greedy_solution,
}

# endregion


def eight_queens(n, solution_function=greedy_solution):
    return solution_function(n)


def main(n_queens, solution=greedy_solution, print_solutions=False, print_profiling_results=False, *args, **kwargs):
    print(f'Solving problem with {n_queens} queens using {solution} solution')
    n = int(n_queens)
    with profile() as profiling_results:
        solutions = list(eight_queens(n, solution_function=solution_functions[solution]))
    print(f'Found {len(solutions)} solutions')

    if print_solutions:
        for solution in solutions:
            for i in range(n):
                print(''.join(solution[i][j] for j in range(n)))
            print()

    if print_profiling_results:
        print('Profiling results')
        print(profiling_results.getvalue())


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Gives all solutions to the n queens problem')
    parser.add_argument('-n', '--n_queens',
                        default=8,
                        help='the number of queens and side length of the chessboard to fill')
    parser.add_argument('-s', '--solution', choices=solution_functions.keys(),
                        default=next(iter(solution_functions.keys())),
                        help='the technique to use to solve the problem')
    parser_args = parser.parse_args()
    main(**vars(parser_args), print_profiling_results=True)
