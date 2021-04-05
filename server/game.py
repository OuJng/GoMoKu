from chessBoard import *
import random


class game:
    def __init__(self):
        self.board = chessBoard()
        self.playerList = []
        self.playerColor = {}
        self.gameStatus = "wait"
        self.currPlayer = 0
    
    
    def playerRegister(self, id):
        if len(self.playerList) >= 2:
            print("playerRegister Failed: Too much player")
            return "failed"
        if self.gameStatus != "wait":
            print("playerRegister Failed: Game started")
            return "failed"
        self.playerList.append(id)
        self.playerColor[id] = len(self.playerList)    # Set order as color, 1 is white, 2 is black
        return "finish"
    
    def start(self):
        if len(self.playerList) != 2:
            print("start Failed: Not enough player")
            return "failed"
        if self.gameStatus == "playing":
            print("already start")
            return "failed"
        self.gameStatus = "playing"
        self.currPlayer = random.randint(0, 1)
        return "finish"
    
    
    def playerPutChess(self, id, place):
        if self.gameStatus != "playing":
            print("game is down")
            return "failed"
        if id not in self.playerList:
            print("No such player", id)
            return "failed"
        if not self.isPlayersTurn(id):
            print("Not your turn", id)
            return "failed"
        
        color = self.playerColor[id]
        success = self.board.putChess(color, place)
        if not success:
            print("putChess failed.")
            return "failed"
        
        self.switchTurn();
        
        win = self.board.checkWin(place)
        if win:
            print("player", id, "win.")
            self.gameStatus = "end"
            return "win"
        
        return "finish"
    
    
    def getBoard(self):
        return self.board.getBoard()


    def whosTurn(self):
        if self.gameStatus != "playing":
            print("game is down")
            return -1
        return self.playerList[self.currPlayer]
    
    
    def isPlayersTurn(self, id):
        return self.whosTurn() == id


    def switchTurn(self):
        self.currPlayer = (self.currPlayer + 1) % 2
        return
    
    
    def getPlayerList(self):
        return self.playerList


def gameUnitTest():
    print("test begin")
    myGame = game()
    myGame.playerRegister(1024)
    myGame.playerRegister(996)
    myGame.start()
    if myGame.whosTurn() == 1024:
        myGame.playerPutChess(1024, [2, 4])
    myGame.playerPutChess(996, [3,3])
    myGame.playerPutChess(996, [3,3])
    myGame.playerPutChess(552, [3,3])
    myGame.playerPutChess(1024, [2,3])
    if myGame.playerPutChess(996, [3,4]) != "finish":
        print("testFailed 1")
        return
    myGame.playerPutChess(1024, [2,5])
    myGame.playerPutChess(996, [3,5])
    myGame.playerPutChess(1024, [2,6])
    myGame.playerPutChess(996, [3,6])
    if myGame.playerPutChess(1024, [2,7]) == "win":
        myGame.playerPutChess(996, [2,6])
        print("testPass 1024")
        return
    if myGame.playerPutChess(996, [3,7]) == "win":
        print("testPass 996")
        return
    print("testFailed")


if __name__ == '__main__':
    gameUnitTest()
    
    