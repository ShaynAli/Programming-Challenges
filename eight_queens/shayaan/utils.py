from functools import lru_cache
from itertools import chain, product
from contextlib import contextmanager

QUEEN = 'Q'
EMPTY = '.'


# region Helpers


def primary_diagonal_positions(i, j, n):
    for offset in range(-i, n-i):
        row, col = i + offset, j + offset
        if not (0 <= row < n and 0 <= col < n):
            continue
        yield row, col


def secondary_diagonal_positions(i, j, n):
    for offset in range(-i, n-i):
        row, col = i + offset, j - offset
        if not (0 <= row < n and 0 <= col < n):
            continue
        yield row, col


def row_positions(i, j, n):
    return ((i, col) for col in range(n))


def column_positions(i, j, n):
    return ((row, j) for row in range(n))


@lru_cache(maxsize=None)
def threatened_positions(i, j, n):
    return set(chain(
        primary_diagonal_positions(i, j, n),
        secondary_diagonal_positions(i, j, n),
        row_positions(i, j, n),
        column_positions(i, j, n)
    ))


def set_of_positions(n):
    return set((i, j) for i, j in product(range(n), range(n)))


# region Getting the row/column/diagonal from the characteristic value
# If these functions are slow we can use multiprocessing Pool.imap_unordered

def primary_diagonal_for_characteristic(x, n):
    return ((i, n - x + i - 1) for i in range(n - abs(x - n + 1)))


def secondary_diagonal_for_characteristic(x, n):
    return ((i, x - i) for i in range(n - abs(x - n + 1)))


def row_for_characteristic(x, n):
    return ((x, i) for i in range(n))


def column_for_characteristic(x, n):
    return ((i, x) for i in range(n))

# endregion


# region Getting the characteristic value from the position

def primary_diagonal_characteristic_of_position(i, j, n):
    return n + i - j - 1


def secondary_diagonal_characteristic_of_position(i, j, n):
    return i + j


def row_characteristic_of_position(i, j, n):
    return i


def column_characteristic_of_position(i, j, n):
    return j

# endregion


def convert_queen_positions_to_a_board(queen_positions, n):
    board = [[EMPTY for _ in range(n)] for _ in range(n)]
    for i, j in queen_positions:
        board[i][j] = QUEEN
    return board


# endregion


@contextmanager
def profile():
    from cProfile import Profile
    from io import StringIO
    import pstats
    profiler = Profile()
    stats_output = StringIO()
    try:
        profiler.enable()
        yield stats_output
    finally:
        profiler.disable()
        profiler_stats = pstats.Stats(profiler, stream=stats_output).sort_stats(pstats.SortKey.CUMULATIVE)
        profiler_stats.print_stats()
