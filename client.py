from xmlrpc.client import ServerProxy
import uuid
import random

class player:
    info = []
    
    def __init__(self):
        self.info.append(str(uuid.uuid1()))
        self.info.append(random.randint(0, 28088))
        self.server = ServerProxy("http://192.168.242.130:28088", allow_none=True)
        self.server.register(self.info)


    def play(self):
        self.server.playGame(self.info)
    
    
    def getState(self):
        state = self.server.getGameState(self.info)
        state[1] = bool(state[1] == self.info[0])
        return state


    def putChess(self, place):
        res = self.server.putChess(self.info, place)
        return res
    
    def quitGame(self):
        res = self.server.quitGame(self.info)
        return res
