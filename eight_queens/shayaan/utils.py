from itertools import chain, product
from contextlib import contextmanager


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


def threatened_positions(i, j, n):
    return set(chain(
        primary_diagonal_positions(i, j, n),
        secondary_diagonal_positions(i, j, n),
        row_positions(i, j, n),
        column_positions(i, j, n)
    ))


def set_of_positions(n):
    return set((i, j) for i, j in product(range(n), range(n)))

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
