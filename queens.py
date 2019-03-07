#! /usr/bin/env python3

from itertools import permutations

from timer import Timer
from board import Board

def place_queen( board, row=0 ):

    for i in range( board.get_size()):
        if board.check_position( row, i ):
            board.set_position( row, i )
            if board.count_queens() == board.get_size():
                count = board.incr_solution_count()
                # print( "Solution: {}\n".format( count ) + str( board ))
            else:
                place_queen( board, row + 1 )
            board.clear_position( row, i )


def permute_queens( boardsize ):

    solutions = []

    for p in permutations(list(range(boardsize))):
        diag1 = set()
        diag2 = set()

        for i in range(boardsize):
            diag1.add(p[i]+i)
            diag2.add(p[i]-i)

        if boardsize == len(diag1) == len(diag2):
            solutions.append(p)

    return len(solutions)



size = int( input( "Enter the number of rows on the board: " ))

if 3 < size < 100:
    cb = Board( size )
else:
    print("Could not allocate a board of size {}".format( size ))
    exit()

with Timer() as t:
    place_queen( cb )

print( "Number of solutions: {}".format( cb.get_solution_count()))

print("Solution took {:.3f} seconds".format(t.interval))

with Timer() as t:
    solution_count = permute_queens( size )

print( "Number of solutions: {}".format( solution_count ))

print("Solution took {:.3f} seconds".format(t.interval))
