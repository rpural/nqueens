#! /usr/bin/env python3

class Board:
    ''' class Board

    Emulate a chess board, of varying size, with the size given at the time
    of creation.
    '''

    def __init__( self, size=8 ):
        ''' __init__(size)

        Initialize a board, given its size. Size will default to 8, the
        size of a regulation chess board.
        '''
        # print("<init>")
        self._board = []
        self._size = size
        self._solutions = 0
        row = []
        for j in range( self._size ):
            row.append(0)
        for i in range( self._size ):
            self._board.append( row.copy() )
        # print("<init> size=" + str(self._size))

    def get_size( self ):
        ''' get_size()
        Return the size of the board
        '''
        return self._size

    def get_solution_count( self ):
        ''' get_solution_count()
        Get the number of solutions found so far
        '''
        return self._solutions

    def incr_solution_count( self ):
        ''' incr_solution_count()
        Increment the number of solutions found so far
        '''
        self._solutions += 1
        return self._solutions

    def check_position( self, x, y ):
        ''' check_position(x, y)

        Check a board position to be sure that it is available for placement, and
        that no other queen threatens the location. Returns True if a queen can
        safely be placed in the location, and False if the position is threatened,
        if there is already a queen there, or if the location is an invalid board
        position.
        '''
        # print("<check> x = {}, y = {} board(x,y) = {}".format(x, y, self._board[x][y]))

        # Are x and y within range?
        if 0 <= x < self._size and 0 <= y < self._size: 
            pass
        else:
            return False

        # The below code isn't really necessary, as the code following it will also
        # check the individual square as part of the row.

        # Is there a queen at the location?
        # if self._board[x][y]  == 1:
        #     return False

        # Is there a queen anywhere within the location's row?
        if 1 in self._board[x]:
            return False

        # Is there a queen anywhere within the location's column?
        for row in range( self._size ):
            if not ( row == x ):
                if self._board[row][y] == 1:
                    return False

        # Is there a queen anywhere on the two diaginals from the location?
        for row in range( self._size ):
            if not ( row == x ):
                delta = row - x
                if delta < 0:
                    delta = -delta
                    if 0 <= (y + delta) < self._size: 
                        if self._board[row][y+delta] == 1:
                            return False
                    if 0 <= (y - delta) < self._size:
                        if self._board[row][y-delta] == 1:
                            return False

        return True

    def set_position( self, x, y ):
        ''' set_position(x, y)

        Place a queen on the board at the given location.
        '''
        # print("<set> x = {}, y = {}, size = {}".format(x, y, self._size))

        # Are x and y within range?
        if 0 <= x < self._size and 0 <= y < self._size:
            pass
        else:
            print( "out of range: {}")
            return False

        if self._board[x][y] == 0:
            self._board[x][y] = 1
            return True
        else:
            return False

    def clear_position( self, x, y ):
        ''' clear_position(x, y)

        Clear a queen from the given location
        '''
        # print("<clear> x = {}, y = {}, size = {}".format(x, y, self._size))

        # Are x and y within range?
        if 0 <= x < self._size and 0 <= y < self._size:
            self._board[x][y] = 0
        return True

    def count_queens( self ):
        ''' count_queens()

        Count and return the number of queens that have been placed on the board.
        '''

        total = 0
        for i in range(self._size):
            total += sum( self._board[i] )
        return total

    def __str__( self ):
        ''' __str__()

        Create a printable string which represents the current state of the board.
        '''

        # Start by drawing a line above the board
        result = "-" * ( self._size * 2 + 2 ) + "\n"
        for row in range( self._size ):
            result += "|"  # Print the left side of the board
            for col in range( self._size ):
                if self._board[row][col] == 1:
                    result += "Q "  # If a queen, print Q, else print .
                else:
                    result += ". "
            result += "|\n"  # Print the right side of the board
        result += "-" * ( self._size * 2 + 2 ) + "\n"  # Print the board bottom
        return result  # Return the printable board as a text string

if __name__ == "__main__":
    ''' If run as a main program, test the features of Board.
    '''

    b = Board( 8 )  # Create a chess board

    print(b)  # Print the empty board (should be all dots)

    if b.check_position( 3, 3 ):  # Be sure (3,3) is empty (which it should be)
        b.set_position( 3, 3 )    # and place a queen there
    print( b.check_position( 3, 3 ))  # This should print "False"
    print(b)  # Print the board with a queen at (3,3)

    if b.check_position( 4, 4 ):  # Check location (4,4); Shouldn't be available
        b.set_position( 4, 4 )  # Place a queen at (4,4) if (4,4) is available
    if b.check_position( 5, 2 ):  # Check location (5,2); Should be available
        b.set_position( 5, 2 )  # Place a queen at (5,2)
    print(b)  #  Print the board. Should show only two queens

    for i in range(b._size):  # Print a numeric representation of the board
        print( b._board[i] )

    b.clear_position( 3, 3 )  # Remove the queen at (3,3)
    print(b)  # and print the board

    b.set_position( 10, 10 )  # Try to place a queen out of bounds
    b.set_position( 7, 8 )    # And one a bit closer, but still out of bounds
    b.set_position( 6, -1 )   # And one out of bounds at the otehr end
    print(b)  # Print the board (Should still be as above)

    print( b.check_position( 2, 4 ))  # Check several positions on the board
    print( b.check_position( 4, 2 ))
    print( b.count_queens())

    print( b.check_position( 4, 4 ))
    b.set_position( 4, 4 )
    print( b.check_position( 5, 5 ))

    print( b.count_queens())
    print(b)
