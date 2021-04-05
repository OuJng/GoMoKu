from game import game

class center:
    waitingList = []
    playerInfo = {}
    playerState = {}
    games = {}
    
    
    def __init__(self):
        pass
    
    
    def register(self, info):
        if info[0] in self.playerInfo:
            print("player already exist")
            return "failed"
        self.playerInfo[info[0]] = info[1]
        self.playerState[info[0]] = "online"
        return "finish"
    
    
    def playGame(self, info):
        if not self.__validPlayer(info):
            return "failed"
        if len(self.waitingList) > 0:
            p2Info = self.waitingList.pop()
            newGame = game()
            newGame.playerRegister(info[0])
            newGame.playerRegister(p2Info[0])
            self.games[info[0]] = newGame
            self.games[p2Info[0]] = newGame
            self.playerState[info[0]] = "playing"
            self.playerState[p2Info[0]] = "playing"
            newGame.start()
            return "start"
        else:
            self.waitingList.append(info)
            self.playerState[info[0]] = "waiting"
        pass
    
    
    def putChess(self, info, place):
        if not self.__validPlayer(info):
            return "failed"
        if self.playerState[info[0]] != "playing":
            print("putChess failed: Not playing")
            return "failed"
        game = self.games[info[0]]
        res = game.playerPutChess(info[0], place)
        if res == "win":
            self.__gameEnd(game)
        return res
    
    
    def getGameState(self, info):
        if not self.__validPlayer(info):
            return None
        if self.playerState[info[0]] != "playing":
            return self.playerState[info[0]]
        game = self.games[info[0]]
        whosTurn = game.whosTurn()
        board = game.getBoard()
        return whosTurn, board
    
    
    def quitGame(self, info):
        if not self.__validPlayer(info):
            return "failed"
        if self.playerState[info[0]] != "playing":
            return "failed"
        self.playerState[info[0]] = "online"
        if info[0] in self.games:
            self.__gameEnd(games[info[0]])
        return "finish"
     
    
    def deleteUser(self, info):
        if not self.__validPlayer(info):
            return "failed"
        if info[0] in self.games:
            self.__gameEnd(games[info[0]])
        self.playerInfo.pop(info[0])
        self.playerState.pop(info[0])
        return "finish"
    
    
    def __validPlayer(self, info):
        if info[0] not in self.playerInfo:
            print("unvalid user")
            return False
        elif info[1] != self.playerInfo[info[0]]:
            print("unvalid user")
            return False
        return True
    

    def __gameEnd(self, game):
        playerList = game.getPlayerList()
        for player in playerList:
            if player in self.games:
                self.games.pop(player)
            if player in self.playerState:
                self.playerState[player] = "online"
        return
    
    
from xmlrpc.server import SimpleXMLRPCServer
    
if __name__ == "__main__":
    obj = center()
    server = SimpleXMLRPCServer(("0.0.0.0", 28088), allow_none=True)
    server.register_instance(obj)
    print("Listening")
    server.serve_forever()