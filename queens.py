#! /usr/bin/env python3

class Board:

    def __init__( self, size=8 ):
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
        print("<clear> x = {}, y = {}, size = {}".format(x, y, self._size))
        if 0 <= x < self._size and 0 <= y < self._size:
            self._board[x][y] = 0
        return True

    def __str__( self ):
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
