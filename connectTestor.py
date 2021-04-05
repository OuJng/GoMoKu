from xmlrpc.client import ServerProxy

if __name__ == "__main__":
    server = ServerProxy("http://localhost:28088", allow_none=True)
    server.playerRegister(1024)
    server.playerRegister(996)
    server.start()
    server.playerPutChess(1024, [1, 1])
    server.playerPutChess(996, [1, 1])
    server.playerPutChess(1024, [3, 3])
    server.playerPutChess(996, [1, 2])