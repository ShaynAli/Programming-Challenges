# 8 Queens

![One solution to the eight queens puzzle](https://helloacm.com/wp-images/acm/2012/queen.png)

## Problem

Find all possible placements of n queens on a chessboard of size nxn such that no queen threatens another for n >= 4.

A queen is considered to "threaten" another piece when it is on the same row, column, or diagonal.

The winning solution is one which completes the problem in under 5 minutes for the largest value of n.

## Specification

Code in every language is limited by the following conditions:
  * Code execution for each test case is limited to 5 minutes.
  * Code must complete each previous case (1, 2, 3, ..., n-1) in 5 minutes or less before a solution for the next case
  (n) is considered.
  * Solutions must be generated and cannot be encoded within the programs themselves.
  * No external data sources can be used.

### Python
```
def eight_queens(n: int):
    """
    Returns a iterator of objects for which each object, o, satisfies the following:
    o[i][j] represents the piece in the ith row and jth column
    o[i][j] == 'Q' represents a queen at the ith row and jth column
    o[i][j] == '.' represents an empty space
    For example, the following would be a valid entry in the returned iterator for n = 8:
    [
        '.....Q..',
        '...Q....',
        '......Q.',
        'Q.......',
        '.......Q',
        '.Q......',
        '....Q...',
        '..Q.....',
    ]
    """
```
