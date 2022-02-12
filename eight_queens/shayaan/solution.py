""" Solves the n queens problem """
__author__ = 'Shayaan Syed Ali'
__email__ = 'shayaan.syed.ali@gmail.com'


from utils import *


# region Solutions

# TODO: Exploit symmetry

def backtracking_algorithm(n):
    """ Search for a solution greedily and test it's viability """

    def backtracking_algorithm_recursive(remaining_positions, n_remaining_queens):
        """
        Returns the positions of queens via a recursive, greedy, brute force* approach
        *There are minor optimizations made just to make it viable for n ~ 10
        """
        if n_remaining_queens == 1:
            for position in remaining_positions:
                yield [position]
        while remaining_positions:
            position = remaining_positions.pop()
            subsolution_remaining_positions = remaining_positions - threatened_positions(*position, n)
            for subsolution_positions in backtracking_algorithm_recursive(
                    subsolution_remaining_positions, n_remaining_queens - 1):
                yield [position] + subsolution_positions

    solutions = backtracking_algorithm_recursive(set_of_positions(n), n)
    return (convert_queen_positions_to_a_board(solution, n) for solution in solutions)


# These are the keywords to select each algorithm in the parser
solution_functions = {
    'backtracking': backtracking_algorithm,
    'bt': backtracking_algorithm,
}

# endregion


def eight_queens(n, solution_function=backtracking_algorithm):
    return solution_function(n)


def main(n_queens, solution=backtracking_algorithm, print_solutions=False, print_profiling=False, quiet=False):

    def info_print(*args, **kwargs):
        if not quiet:
            print(*args, **kwargs)

    info_print(f'Solving problem with {n_queens} queens using {solution} solution')
    n = int(n_queens)
    with profile() as profiling_results:
        solutions = list(eight_queens(n, solution_function=solution_functions[solution]))
    info_print(f'Found {len(solutions)} solutions')

    if print_solutions:
        for solution in solutions:
            for i in range(n):
                print(''.join(solution[i][j] for j in range(n)))
            print()

    if print_profiling:
        info_print('Profiling results')
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
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='if provided, executes without informational output')
    parser.add_argument('-ps', '--print-solutions', action='store_true',
                        help='if provided, prints all found solutions')
    parser.add_argument('-pp', '--print-profiling', action='store_true',
                        help='if provided, prints profiling results from cProfile')
    parser_args = parser.parse_args()
    main(**vars(parser_args))
