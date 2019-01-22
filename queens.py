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
        print("<init>")
        self._board = []
        self._size = size
        row = []
        for j in range( self._size ):
            row.append(0)
        for i in range( self._size ):
            self._board.append( row.copy() )
        print("<init> size=" + str(self._size))

    def check_position( self, x, y ):
        ''' check_position(x, y)

        Check a board position to be sure that it is available for placement, and
        that no other queen threatens the location. Returns True if a queen can
        safely be placed in the location, and False if the position is threatened,
        if there is already a queen there, or if the location is an invalid board
        position.
        '''
        print("<check> x = {}, y = {} board(x,y) = {}".format(x, y, self._board[x][y]))
        if 0 <= x < self._size: 
            pass
        else:
            return False
        if 0 <= y < self._size:
            pass
        else:
            return False
        if self._board[x][y]  == 1:
            return False
        if 1 in self._board[x]:
            return False

        for row in range( self._size ):
            if not ( row == x ):
                if self._board[row][y] == 1:
                    return False

        return True

    def set_position( self, x, y ):
        ''' set_position(x, y)
        
        Place a queen on the board at the given location.
        '''
        print("<set> x = {}, y = {}, size = {}".format(x, y, self._size))
        if 0 <= x < self._size:
            pass
        else:
            print( "x out of range: {}".format(x))
            return False
        if 0 <= y < self._size:
            pass
        else:
            print( "y out of range: {}".format(y))
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
        print("<clear> x = {}, y = {}, size = {}".format(x, y, self._size))
        if 0 <= x < self._size and 0 <= y < self._size:
            self._board[x][y] = 0
        return True

    def __str__( self ):
        ''' __str__()

        Create a printable string which represents the current state of the board.
        '''
        result = "-" * ( self._size * 2 + 2 ) + "\n"
        for row in range( self._size ):
            result += "|"
            for col in range( self._size ):
                if self._board[row][col] == 1:
                    result += "Q "
                else:
                    result += ". "
            result += "|\n"
        result += "-" * ( self._size * 2 + 2 ) + "\n"
        return result

if __name__ == "__main__":
    ''' If run as a main program, test the features of Board.
    '''

    b = Board( 8 )

    print(b)

    if b.check_position( 3, 3 ):
        b.set_position( 3, 3 )
    print( b.check_position( 3, 3 ))
    print(b)

    b.set_position( 4, 4 )
    print(b)

    for i in range(b._size):
        print( b._board[i] )

    print(b)

    b.clear_position( 3, 3 )
    print(b)

    b.set_position( 10, 10 )
    b.set_position( 7, 8 )
    b.set_position( 6, -1 )
    print(b)

    print( b.check_position( 2, 4 ))
    print( b.check_position( 4, 2 ))
    print( b.check_position( 4, 4 ))
    print( b.check_position( 5, 5 ))
