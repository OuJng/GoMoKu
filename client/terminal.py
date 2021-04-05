from client import player
import re

class terminal:
    playCommand = ["play", "play game", "start game", "join game"]
    quitCommand = ["quit", "quit game", "exit game"]
    exitCommand = ["exit"]
    putCommand = ["put", "put chess"]

    def __init__(self):
        self.client = player()
        return


    def play(self):
        self.client.play()
        return


    def put(self, place):
        self.client.putChess(place)
        return


    def quit(self):
        self.client.quitGame()
        return


    def run(self):
        while True:
            inputStr = input(">> ")
            self.parseInput(inputStr)
            self.refreshState()
            
        
    def parseInput(self, inputStr):
        slist = re.split("[ ,.:]", inputStr.strip("[] \n"))
        ilist = [int(num) for num in slist if num.strip().isdigit()]
        if "play" in slist:
            self.play()
        elif "quit" in slist:
            self.quit()
        elif len(ilist) == 2:
            self.put(ilist)
        

    def refreshState(self):
        state = self.client.getState()
        stateStr = state[0]
        myTurn = state[1]
        board = state[2]
        if stateStr == "error":
            print("error: server connection failed")
        elif stateStr == "playing":
            strBoard = self.makeBoard(board)
            for string in strBoard:
                print(string)
            if myTurn:
                print("your turn.")
            else:
                print("waiting.")
        else:
            print("current status: ", stateStr)
        return


    def makeBoard(self, board):
        rowNum = len(board)
        colNum = len(board[0])

        string = "  "
        for i in range(0, colNum):
            string += (str(i) + " ")
        
        stringList = [string]

        for i in range(0, rowNum):
            string = str(i) + " "
            map = {0: "-", 1: "X", 2: "O"}
            chessRow = [map[num] for num in board[i]]
            for char in chessRow:
                string += (char + " ")
            stringList.append(string)
        
        return stringList


if __name__ == "__main__":
    myTerminal = terminal()
    myTerminal.run()