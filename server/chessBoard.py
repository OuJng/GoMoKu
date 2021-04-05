

boardSize = [10, 10]


class chessBoard:
    empty = 0
    white = 1
    black = 2
    
    def __init__(self):
        self.rowNum = boardSize[0]
        self.colNum = boardSize[1]
        self.board = [[self.empty for i in range(self.colNum)] for i in range(self.rowNum)]
        
        
    def printBoard(self):
        for row in self.board:
            print(row)
            
            
    def getBoard(self):
        return self.board
        
        
    def putChess(self, color, place):
        originColor = self.board[place[0]][place[1]]
        if originColor != self.empty:
            print("putChess failed: Not empty")
            return False
        self.board[place[0]][place[1]] = color
        return True
        
        
    def checkWin(self, place):
        color = self.board[place[0]][place[1]]
        
        if color == self.empty:
            print("checkWin failed: checking empty place")
            return False
        
        directionPairs = [[[-1, 0], [1, 0]], [[0, -1], [0, 1]], [[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]
        for directionPair in directionPairs:
            count = 0
            for direct in directionPair:
                idx = [place[0] + direct[0], place[1] + direct[1]]
                while self.valid(idx) and self.board[idx[0]][idx[1]] == color:
                    count += 1
                    idx[0] += direct[0]
                    idx[1] += direct[1]
            if count >= 4:
                return True
        return False
    
    
    def valid(self, index):
        if 0 <= index[0] < self.rowNum and 0 <= index[1] < self.colNum:
            return True
        return False
    

def chessBoardTestCase():
    print("start test")
    board = chessBoard()

    for ri in range(1, 4):
        board.putChess(1, [ri, ri])
    for ri in range(3, 7):
        board.putChess(1, [ri, 2])
        
    if board.checkWin([3, 2]):
        print("testCase 1 pass")
    
    for ri in range(2, 7):
        board.putChess(2, [ri, 9])
    if board.checkWin([4, 9]):
        print("testCase 2 pass")
        
    for i in range(4, 9):
        board.putChess(2, [i, i])
    for i in range(4, 9):
        if not board.checkWin([i, i]):
            print("testCase 3 failed")
            return
    print("testCase 3 pass")
    
if __name__ == '__main__':
    chessBoardTestCase()    
