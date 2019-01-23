#! /usr/bin/env python3

from board import Board

def place_queen( board, row=0 ):

    for i in range( board.get_size()):
        if board.check_position( row, i ):
            board.set_position( row, i )
            if board.count_queens() == board.get_size():
                print( "Solution: {}\n".format( board.incr_solution_count()) + str( board ))
            else:
                place_queen( board, row + 1 )
            board.clear_position( row, i )


size = int( input( "Enter the number of rows on the board: " ))

if 3 < size < 100:
    cb = Board( size )
else:
    print("Could not allocate a board of size {}".format( size ))
    exit()

place_queen( cb )

print( "Number of solutions: {}".format( cb.get_solution_count()))
