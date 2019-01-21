#! /usr/bin/env python3

class Board:

    def __init__( self, size=8 ):
        print("<init>")
        self._board = []
        self._size = size
        for i in range( self._size ):
            row = []
            for j in range( self._size ):
                row.append(0)
            self._board.append( row.copy() )
        print("<init> size=" + str(self._size))

    def check_position( self, x, y ):
        print("<check> x = {}, y = {} board(x,y) = {}".format(x, y, self._board[x][y]))
        if -1 < x < self._size: 
            pass
        else:
            return False
        if -1 < y < self._size:
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
        if -1 < y < self._size:
            pass
        else:
            print( "y out of range: {}".format(y))
            return False

        if self._board[x][y] == 0:
            self._board[x][y] = 1
            return True
        else:
            return False

    def __str__( self ):
        result = "-" * self._size + "\n"
        for row in range( self._size ):
            for col in range( self._size ):
                if self._board[row][col] == 1:
                    result += "Q"
                else:
                    result += "."
            result += "\n"
        result += "-" * self._size + "\n"
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
